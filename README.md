# 🤖 Multi-Modal Autonomous Mobile Manipulator

> **Project Type:** Capstone Robotics Project  

A capstone robotics project focused on developing a multi-modal autonomous mobile manipulator capable of combining mobile navigation, robotic arm manipulation, perception, and embedded control into a single robotic platform.

The system integrates ROS 2, Nav2, SLAM, MoveIt 2, computer vision, LiDAR, ESP32-based actuator control, and Raspberry Pi 5 to create a mobile robot capable of autonomous navigation and object manipulation.

---

## 👥 Team & Acknowledgments

**Department of Electronics & Communication Engineering**  
**Mangalore Institute of Technology & Engineering**

### Team Members
* **K M Thejas** — 4MT23EC030
* **Tashvi Prasad** — 4MT23EC001
* **Chinmay Devaramani** — 4MT23EC016
* **Manjunatha K** — 4MT23EC039

### Project Guide
* **Mr. Uday J**  
  Senior Assistant Professor  
  Department of Electronics & Communication Engineering

---

## 🚀 Project Overview

The goal of this project is to develop an autonomous mobile robot equipped with a robotic manipulator that can:

* 🗺️ Build and use maps of its environment using LiDAR and SLAM
* 🧭 Navigate autonomously using ROS 2 Nav2
* 👁️ Detect and identify objects using YOLO-based computer vision
* 🦾 Plan and execute robotic arm movements using MoveIt 2
* 🤖 Control servo motors through an ESP32
* 📡 Communicate between high-level ROS 2 software and embedded hardware
* 🧠 Combine perception, navigation, and manipulation into one robotic system
* 💻 Run the robotics software end on a Raspberry Pi 5

---

## 📈 Progress Till Date

**Current Status:** The robotic arm hardware assembly and MoveIt 2 software setup are fully complete. 

We have successfully modeled the 5-DOF manipulator using URDF/Xacro, integrated it with ROS 2, and established a working motion planning pipeline using MoveIt 2 in RViz. The ESP32 circuit prototype for physical servo actuation has also been built and tested. 

<p align="center">
  <img src="https://github.com/user-attachments/assets/14f3a37d-0a93-4444-87ae-3083547fe138" width="32%">
  <img src="https://github.com/user-attachments/assets/c9afa44a-a1d6-45f1-89c0-a21aa7ad3ff2" width="32%">
  <img src="https://github.com/user-attachments/assets/1ddf0196-409f-45e1-a833-d794ed7d34dd" width="32%">
</p>

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────────┐
                    │       Raspberry Pi 5    │
                    │                         │
                    │          ROS 2          │
                    │                         │
                    │  ┌───────┐  ┌─────────┐ │
                    │  │ Nav2  │  │ MoveIt2 │ │
                    │  └───┬───┘  └────┬────┘ │
                    │      │             │    │
                    │  ┌───▼─────────────▼───┐│
                    │  │     ROS 2 Nodes     ││
                    │  └──────────┬──────────┘│
                    │             │           │
                    │      ┌──────▼──────┐    │
                    │      │ Perception  │    │
                    │      │ YOLO / CV   │    │
                    │      └─────────────┘    │
                    └─────────────┬───────────┘
                                  │
                           micro-ROS / Serial
                                  │
                         ┌────────▼────────┐
                         │      ESP32      │
                         │                 │
                         │ Servo Control   │
                         │ Motor Control   │
                         └───────┬─────────┘
                                 │
              ┌──────────────────┴──────────────────┐
              │                                     │
        ┌─────▼─────┐                         ┌─────▼─────┐
        │ Mobile    │                         │ Robotic   │
        │ Base      │                         │ Arm       │
        └───────────┘                         └───────────┘

                    ┌─────────────────┐
                    │     YDLIDAR     │
                    │                 │
                    │ Mapping / SLAM  │
                    └─────────────────┘

```

---

## 🧩 Main Technologies

| Component | Technology |
| --- | --- |
| **Robotics Middleware** | ROS 2 |
| **Navigation** | Nav2 |
| **Manipulation** | MoveIt 2 |
| **Mapping** | SLAM Toolbox |
| **Perception** | YOLO / Computer Vision |
| **LiDAR** | YDLIDAR X2L / 2XL |
| **Main Computer** | Raspberry Pi 5 |
| **Embedded Controller** | ESP32 |
| **Embedded Communication** | micro-ROS |
| **Actuators** | Servo Motors |
| **Robot Description** | URDF / Xacro |
| **Visualization** | RViz 2 |
| **Simulation / Planning** | ROS 2 + MoveIt 2 |

---

## 🦾 Robotic Manipulator

The robotic arm is modeled using URDF/Xacro and integrated with ROS 2 and MoveIt 2 for trajectory execution and hardware control.

### Hardware & Simulation Integration Flow

The manipulation subsystem translates high-level Cartesian/joint goal states into physical servo motion through a 3-step pipeline:

#### Step 1: Kinematic Modeling & Interactive Trajectory Planning (RViz & MoveIt 2)

The arm kinematic chain is solved in real time using MoveIt 2's OMPL/KDL plugins to verify collision boundaries and generate smooth joint trajectories.

#### Step 2: Workstation Development & Serial Communication Pipeline

The ROS 2 environment interfaces directly with the host development workstation, routing serialized joint angles from the MoveIt 2 pipeline down to the microcontroller bridge.

#### Step 3: Low-Level Actuation via ESP32 Hardware

The ESP32 microcontroller receives target joint positions via micro-ROS and generates multi-channel PWM signals to drive each servo motor synchronously on the physical arm assembly.

### Arm Joints

* `base_joint`
* `shoulder_joint`
* `elbow_joint`
* `wrist_roll_joint`
* `wrist_pitch_link`
* `finger_gripper_joint`

MoveIt 2 is used for:

* Motion planning
* Joint-space planning
* Collision checking
* End-effector control
* Manipulator visualization
* Trajectory generation

The generated joint trajectories are converted into actuator commands and sent to the ESP32.

---

## 🛞 Mobile Platform

The mobile base provides autonomous movement and navigation.

The platform integrates:

* Drive wheels
* Swivel caster wheels
* Motor control
* LiDAR
* Raspberry Pi 5
* ESP32-based embedded control

The robot is intended to operate in indoor environments and navigate between different locations while carrying the robotic manipulator.

---

## 🗺️ SLAM & Navigation

A YDLIDAR sensor is used to obtain laser scan data.

ROS 2 processes the LiDAR data through SLAM Toolbox to generate an occupancy grid map.

```text
YDLIDAR
   │
   ▼
/scan
   │
   ▼
SLAM Toolbox
   │
   ├── /map
   └── /map_metadata
          │
          ▼
         Nav2
          │
          ▼
    Autonomous Navigation

```

The navigation stack is based on ROS 2 Nav2.

---

## 👁️ Computer Vision & Object Detection

The perception subsystem is designed around YOLO-based object detection.

The vision system can be used to:

* Capture camera frames
* Detect objects
* Identify the target object
* Estimate the object's location
* Provide the target information to the manipulation system
* Plan a suitable arm motion using MoveIt 2

Future integration can combine camera-based perception with LiDAR data for improved environmental understanding.

---

## 🔌 ESP32 & Embedded Control

The ESP32 acts as the low-level controller for the robotic hardware.

ROS 2 communicates with the ESP32 through micro-ROS.

Example communication flow:

```text
MoveIt 2
    │
    ▼
/joint_states
    │
    ▼
ROS 2 Bridge
    │
    ▼
/joint_commands
    │
    ▼
micro-ROS Agent
    │
    ▼
ESP32
    │
    ▼
Servo Motors

```

The embedded controller handles actuator-level commands while ROS 2 performs high-level planning and coordination.

---

## 💻 Software Requirements

Recommended environment:

* Ubuntu 24.04
* ROS 2 Jazzy
* Python 3
* Git
* RViz 2
* MoveIt 2
* Nav2
* SLAM Toolbox
* micro-ROS

The project can also be developed and tested in a ROS 2 development environment before deployment to the Raspberry Pi 5.

---

## 📁 Repository Structure

```text
.
├── .gitignore
├── README.md
└── src/
    ├── Robotic_description/
    │   ├── config/
    │   ├── launch/
    │   ├── meshes/
    │   ├── resource/
    │   ├── urdf/
    │   ├── package.xml
    │   └── setup.py
    └── Robotic_moveit_config/
        ├── config/
        ├── launch/
        ├── package.xml
        └── setup.py

```

*Additional modules (micro_ros_ws, navigation, slam, perception, firmware) will be integrated as development progresses.*

---

## 🔄 Overall System Workflow

```text
                 START
                   │
                   ▼
            Sensor Acquisition
                   │
          ┌────────┴────────┐
          │                 │
       LiDAR              Camera
          │                 │
          ▼                 ▼
        SLAM              YOLO
          │                 │
          ▼                 ▼
       Mapping        Object Detection
          │                 │
          └────────┬────────┘
                   │
                   ▼
          Autonomous Navigation
                  Nav2
                   │
                   ▼
             Target Location
                   │
                   ▼
               MoveIt 2
                   │
                   ▼
           Motion Planning
                   │
                   ▼
                ESP32
                   │
                   ▼
             Servo Control
                   │
                   ▼
             Object Grasping

```

---

## 🎯 Project Objectives

### Phase 1 — Robot Modeling

* [x] Create robot URDF/Xacro
* [x] Configure robot joints
* [x] Add meshes
* [x] Visualize robot in RViz
* [x] Configure joint limits

### Phase 2 — Manipulator Control

* [x] Configure `Robotic_moveit_config` package
* [x] RViz Motion Planning scene integration
* [x] Prototype physical arm circuit on ESP32 breadboard
* [ ] Finalize joint trajectory execution over micro-ROS
* [ ] Calibrate physical servo limits against URDF bounds

### Phase 3 — Mobile Navigation

* [ ] Integrate mobile base
* [ ] Integrate LiDAR
* [ ] Configure SLAM
* [ ] Generate environment maps
* [ ] Configure Nav2
* [ ] Test autonomous navigation

### Phase 4 — Perception

* [ ] Integrate camera
* [ ] Implement YOLO object detection
* [ ] Connect object detection with ROS 2
* [ ] Estimate target position
* [ ] Integrate perception with manipulation

### Phase 5 — Full System Integration

* [ ] Integrate navigation and manipulation
* [ ] Perform autonomous object navigation
* [ ] Detect target objects
* [ ] Navigate to target
* [ ] Position manipulator
* [ ] Grasp object
* [ ] Transport object
* [ ] Release object

---

## 🔮 Future Development

Potential future improvements include:

* Multi-sensor fusion
* Visual SLAM
* Depth-camera integration
* Object pose estimation
* Autonomous grasp planning
* Edge AI optimization
* Improved obstacle avoidance
* Multi-robot coordination
* AI-based task planning

---

## 📜 License

This project is developed as an academic capstone project.

License and contribution guidelines will be added as the project progresses.

```

```
