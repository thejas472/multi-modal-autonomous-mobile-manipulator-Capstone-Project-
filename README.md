# Multi-Modal Autonomous Mobile Manipulator

## Overview

Development of a multi-modal autonomous mobile manipulator using ROS 2.

The system combines a mobile robot base, robotic arm, perception, navigation, and manipulation into a single autonomous robotic platform.

## Main Technologies

- ROS 2 Humble
- MoveIt 2
- Nav2
- SLAM
- YOLO
- micro-ROS
- Raspberry Pi 5
- ESP32

## Robot Components

- Differential-drive mobile base
- 5-DOF robotic arm
- Gripper
- LiDAR
- USB camera
- IMU
- Wheel encoders
- Raspberry Pi 5
- ESP32

## System Pipeline

Camera → Object Detection → Navigation Goal → SLAM / Localization → Nav2 → Mobile Base → Target Object → MoveIt 2 → Robotic Arm → Pick and Place

## Current Progress

### Completed

- ROS 2 Humble setup
- Robotic arm URDF/Xacro
- 5-DOF robotic arm model
- Gripper model
- MoveIt 2 configuration
- MoveIt 2 planning
- RViz visualization
- ESP32 / micro-ROS integration

### In Progress

- Mobile robot base
- LiDAR integration
- SLAM
- Nav2 navigation
- Wheel encoder integration

### Planned

- YOLO object detection
- Camera integration
- Autonomous navigation
- Autonomous pick and place
- High-level decision making
- Full system integration

## Repository Structure

```text
src/
├── Robotic_description/
└── Robotic_moveit_config/

docs/
└── progress/