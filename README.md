# PICK-AND-PLACE - CoppeliaSim + Python Remote API
Pick-and-Place simulation using ABB IRB140 robot in CoppeliaSim, controlled via Python Remote API (ZMQ).  Includes the simulation scene (.ttt) and Python script for smooth object manipulation with gripper control.



## 📂 Repository Contents
- `pick and place.ttt` → CoppeliaSim scene file containing the IRB140 robot, gripper, object, and targets.
- `pick_and_place.py` → Python script implementing the pick-and-place sequence:
  - Open gripper
  - Move above the object
  - Grip the object
  - Lift smoothly
  - Place object at target location
  - Release gripper

---

## 🚀 Features
- Smooth motion interpolation for robot path
- Gripper control (open, close, hold)
- Object parenting/unparenting for realistic grasp
- Step-based simulation control via Remote API
- Customizable targets for flexible pick-and-place tasks

---

## ⚙️ Requirements
- **CoppeliaSim Edu / Pro** (tested with latest EDU)
- **Python 3.8+**
- **Dependencies**:
  ```bash
  pip install coppeliasim-zmqremoteapi-client


▶️ How to Simulate

Open the Scene in CoppeliaSim

Launch CoppeliaSim.

Open the file:

pick and place.ttt


Ensure Remote API is Enabled

In CoppeliaSim, the ZMQ Remote API is enabled by default in recent versions.

Keep the simulation stopped — the Python script will control starting and stepping the sim.

Run the Python Script

Open a terminal in your project folder.

Execute:

python pick_and_place.py


Watch the Simulation 🎥

The robot will:

Open the gripper

Move above the object

Grip the object

Lift it smoothly

Move to the target position

Release the object

Stop Simulation (optional)

Once finished, the script will stop sending steps.

You can manually stop the simulation in CoppeliaSim if needed.

📸 Demo

The IRB140 robot smoothly picks an object from the table and places it at a target location using the gripper.
(Add a GIF or screenshot here for better presentation)

📜 License

This project is open-source under the MIT License.


---
