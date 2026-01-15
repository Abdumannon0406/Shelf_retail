Shelf Retail Detection & Segmentation
        Project Overview

This project automates quality control for shelving units before packaging. It detects shelves inside boxes and segments key components for verification.

Two models are used:

        Shelf Detection – Detects each shelf in a box.
        
        Shelf Component Segmentation – For each cropped shelf, segments antiplifir, bullnose, and divider.
        
        Purpose: Ensures correct assembly and placement of shelving components prior to shipment.

Computer Vision Tasks:

        Detection: Object detection for shelves
        
        Segmentation: YOLO-based segmentation for shelf components

Dataset:

        Type: Fully custom
        
        Annotation Tools: CVAT

Models & TrainingL:

        YOLO Version: YOLOv11-n

Framework: PyTorch

Hardware: GPU (e.g., RTX 4080 Super)

Image Size: Used consistently across both models

Training Time: Optimized per model

Techniques Used:

Transfer learning

Class balancing

Custom anchors

Inference Pipeline
        +----------------+
        | Input (Image)  |
        +----------------+
                 |
                 v
        +----------------+
        | Shelf Detection|
        +----------------+
                 |
                 v
        +----------------+
        | Crop Shelves   |
        +----------------+
                 |
                 v
+----------------+----------------+
| Shelf Component Segmentation     |
| - Antiplifir                     |
| - Bullnose                       |
| - Divider                        |
+----------------+----------------+
                 |
                 v
        +----------------+
        | Output         |
        | - Checked      |
        |   videos       |         |
        +----------------+

Usage

Input Types: Image, video, or live camera stream

Operation: Real-time capable or offline inspection

Output: Annotated images and JSON

Project Structure
├── data/
│   ├── train/
│   └── val/
├── models/
├── scripts/
├── outputs/
└── README.md

Installation & Requirements

Python Version: 3.x

Dependencies: PyTorch, YOLOv11, OpenCV, NumPy

Install:

pip install -r requirements.txt

Deployment

Compatible with local GPU or edge devices

Video inference supported

Audience & Tone

Targeted for developers, clients, and portfolio presentation

Technical, professional, and easy to understand
