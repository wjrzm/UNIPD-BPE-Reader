# UNIPD-BPE-Reader Dataset Parsing Tool 

## Introduction

This project is a tool designed to parse and analyze datasets. It aims to simplify the process of reading, cleaning, and extracting valuable insights from various types of data files. It is a python reader of the [Dataset-UNIPD-BPE](https://www.mdpi.com/2306-5729/7/6/79). 

<h1 align='Center'>UNIPD-BPE: Synchronized RGB-D and Inertial Data for Multimodal Body Pose Estimation and Tracking</h1>

![image](https://github.com/user-attachments/assets/1d6b2a62-941b-413b-8ee0-3e3dde7be513)

## Usage 

1. Prepare your dataset and place it in the `data/` directory.
2. Process xsens data for imu data: ```python mvnxReader.py```
3. Process rosbag data for video: ```python rosbagReader.py```

## Contributing 

We welcome contributions to enhance the functionality and usability of this tool. 
## License 

This project is licensed under the MIT License. See the `LICENSE` file for more details. 
