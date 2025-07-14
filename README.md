## Overview
This repository contains code, documentation, and results from my work on debugging and validating AI model implementations for deployment on edge devices. The project focused on identifying and correcting issues in existing code sourced from Stack Overflow and verifying functionality and performance using test datasets.

## Objectives
- Analyze community-sourced AI model code for correctness and efficiency.
- Debug implementation errors affecting output accuracy.
- Validate the corrected code with representative test data.
- Assess performance for potential use on resource-constrained edge devices.

## Approach
1. **Code Review and Debugging**  
   - Identified logical and structural issues in publicly shared example code.
   - Refactored the code to improve readability and maintainability.

2. **Validation**  
   - Created test cases to verify that the corrected code produced expected outputs.
   - Measured runtime performance and resource utilization.

3. **Results**  
   - Confirmed correct functionality across multiple datasets.
   - Documented improvements in execution consistency and efficiency.
  
## 🧠 Machine Learning Model
A lightweight YOLOv8-based **image classification** model (`yolo11n-cls.pt`) was used for training and testing.  
The model was built and deployed using the [Ultralytics YOLO](https://docs.ultralytics.com/) Python library.

This model was tested on the Jetson Orin Nano Edge Device

Key characteristics:
- Classifies images into categories (e.g., “hazard” or “clean”)
- Trained using transfer learning from a pre-trained YOLOv8 checkpoint
- Inference run on both single images and directories of test images

## 📊 Dataset

The project used a custom image dataset called `hazard_dataset`, which contained labeled images organized in YOLO format:

## 🧪 Output

The training script produces logs of:
- Accuracy (`top1`, `top5`)
- Inference speed
- Memory usage
- Training loss and fitness

Example:
<img width="1201" height="469" alt="image" src="https://github.com/user-attachments/assets/9cc3269a-dc93-4c2d-8c0a-eee2a1c0aac6" />

