# -*- coding: utf-8 -*-
"""Copy of Testing&Results.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B5Jf_KtOwM-P_IFZ_HxcdmQ6vW79CNR1
"""

!unzip hazard_dataset-20250213T233014Z-001.zip

!pip install ultralytics

from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n-cls.yaml")  # build a new model from YAML
model = YOLO("yolo11n-cls.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo11n-cls.yaml").load("yolo11n-cls.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="datasets/hazard_dataset", epochs=100, imgsz=64)

model.val()

result = model.predict("/content/hazard_dataset/test/clean_1.jpg")

model.predict("/content/hazard_dataset/test")