from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time

# Connect to CoppeliaSim
client = RemoteAPIClient()
sim = client.getObject('sim')

sim.setStepping(True)
sim.startSimulation()
time.sleep(0.5)

# Object handles
ik_target = sim.getObject('/IRB140/target')
target1 = sim.getObject('/target1')
target2 = sim.getObject('/target2')
target3 = sim.getObject('/target3')

j1 = sim.getObject('/active1')
j2 = sim.getObject('/active2')

object_handle = sim.getObject('/object')
gripper_tip = sim.getObject('/connection')

# Smooth move with interpolation and optional holding
def move_to_dummy(dummy, steps=30, delay=0.05, hold=False):
    pos = sim.getObjectPosition(dummy, -1)
    orient = sim.getObjectQuaternion(dummy, -1)
    start_pos = sim.getObjectPosition(ik_target, -1)
    start_orient = sim.getObjectQuaternion(ik_target, -1)

    for i in range(steps):
        interp_pos = [start_pos[j] + (pos[j] - start_pos[j]) * (i / steps) for j in range(3)]
        interp_quat = [start_orient[j] + (orient[j] - start_orient[j]) * (i / steps) for j in range(4)]
        sim.setObjectPosition(ik_target, -1, interp_pos)
        sim.setObjectQuaternion(ik_target, -1, interp_quat)
        
        if hold:
            hold_gripper_closed()
        
        sim.step()
        time.sleep(delay)

# Gripper controls
def open_gripper(timeout=2.0):
    start_time = time.time()
    while time.time() - start_time < timeout:
        sim.setJointTargetVelocity(j1, 0.04)
        sim.setJointTargetVelocity(j2, 0.04)
        sim.step()
        time.sleep(0.01)
    sim.setJointTargetVelocity(j1, 0)
    sim.setJointTargetVelocity(j2, 0)

def hold_gripper_closed():
    sim.setJointTargetVelocity(j1, -0.02)
    sim.setJointTargetVelocity(j2, -0.02)

def stop_gripper():
    sim.setJointTargetVelocity(j1, 0)
    sim.setJointTargetVelocity(j2, 0)

def close_gripper(timeout=3.0):
    start_time = time.time()
    while time.time() - start_time < timeout:
        p1 = sim.getJointPosition(j1)
        p2 = sim.getJointPosition(j2)
        if p1 < p2 - 0.005:
            sim.setJointTargetVelocity(j1, -0.02)
            sim.setJointTargetVelocity(j2, -0.06)
        else:
            sim.setJointTargetVelocity(j1, -0.06)
            sim.setJointTargetVelocity(j2, -0.06)
        sim.step()
        time.sleep(0.01)
    stop_gripper()
    sim.setObjectParent(object_handle, gripper_tip, True)

# Vertical lift after gripping
def slow_lift(z_lift=0.15, steps=60, delay=0.05):
    pos = sim.getObjectPosition(ik_target, -1)
    target_pos = [pos[0], pos[1], pos[2] + z_lift]
    for i in range(steps):
        interp = [pos[j] + (target_pos[j] - pos[j]) * (i / steps) for j in range(3)]
        sim.setObjectPosition(ik_target, -1, interp)
        hold_gripper_closed()
        sim.step()
        time.sleep(delay)
    stop_gripper()

# Make object light for easy gripping
sim.setShapeMass(object_handle, 0.01)

# --- Main Pick and Place Sequence ---

open_gripper(timeout=2.0)                               # Step 1: Open gripper
move_to_dummy(target1, steps=60, delay=0.04)            # Step 2: Move above object
move_to_dummy(target2, steps=60, delay=0.04)            # Step 3: Move to object surface
close_gripper(timeout=3.0)                              # Step 4: Grip the object
slow_lift(z_lift=0.15, steps=60, delay=0.04)            # Step 5: Lift object slowly

# Step 6: Move to place location in 2 parts (horizontal + vertical)
current_pos = sim.getObjectPosition(ik_target, -1)
final_pos = sim.getObjectPosition(target3, -1)
mid_pos = [final_pos[0], final_pos[1], current_pos[2]]

mid_dummy = sim.createDummy(0.01)
sim.setObjectPosition(mid_dummy, -1, mid_pos)
sim.setObjectQuaternion(mid_dummy, -1, sim.getObjectQuaternion(target3, -1))

move_to_dummy(mid_dummy, steps=80, delay=0.04, hold=True)
move_to_dummy(target3, steps=60, delay=0.04, hold=True)
sim.removeObject(mid_dummy)

sim.setObjectParent(object_handle, -1, True)            # Step 7: Release object
open_gripper(timeout=2.0)                               # Step 8: Open gripper

print(" Pick-and-place completed slowly and smoothly.")