# PICK-AND-PLACE
Pick-and-Place simulation using ABB IRB140 robot in CoppeliaSim, controlled via Python Remote API (ZMQ).  Includes the simulation scene (.ttt) and Python script for smooth object manipulation with gripper control.



# 🤖 Pick and Place – CoppeliaSim + Python Remote API

This project demonstrates a **Pick-and-Place simulation using the **ABB IRB140 robot** with a gripper in **CoppeliaSim**, controlled via Python using the **ZMQ Remote API**.

---

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
