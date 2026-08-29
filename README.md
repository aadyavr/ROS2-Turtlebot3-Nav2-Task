# TurtleBot 3 SLAM & Nav2 Task 1

## Overview
This repository contains the setup, launch files, generated maps, and conceptual documentation for Task 1, covering ROS 2 Humble, Gazebo simulation, SLAM mapping, and Navigation 2 (Nav2).

---

## Conceptual Explanations & Answers

### 1. Key Concepts
* **Localization**: The process of estimating the robot's precise position and orientation $(x, y, \theta)$ relative to a known map frame.
* **SLAM (Simultaneous Localization and Mapping)**: The process of building a 2D occupancy grid map of an unknown environment while simultaneously tracking the robot's position within it.
* **Nav2 (Navigation 2)**: The ROS 2 navigation stack that processes static map data, real-time sensor streams, local/global costmaps, and localization to autonomously plan collision-free paths and steer the robot toward a goal pose.

### 2. Visualization & Flow Chart Command
* **Node & Topic Data Flow**: `rqt_graph` visualizes the active ROS 2 computational graph, showing interactive nodes and topic publisher/subscriber connections.
* **TF Transform Tree**: `ros2 run tf2_tools view_frames` generates a visual PDF (`frames.pdf`) detailing the transformation tree between frames (`map` $\rightarrow$ `odom` $\rightarrow$ `base_footprint` $\rightarrow$ `base_link`).

---

## Repository Structure
```text
turtlebot3_nav2_task1/
├── launch/
│   └── bringup_all.launch.py   # Unified launch script for Gazebo & Nav2
├── maps/
│   ├── my_map.yaml             # Map metadata configuration
│   └── my_map.pgm              # Occupancy grid map image
├── rqt_graph.png               # Computational node graph screenshot
└── README.md                   # Project documentation
