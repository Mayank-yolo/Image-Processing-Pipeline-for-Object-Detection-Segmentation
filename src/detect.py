# src/detect.py

from ultralytics import YOLO
import os

def detect_objects(model_path, processed_data_path, output_path):
    print("🚀 Starting Object Detection...")

    # Load YOLOv8 model
    try:
        model = YOLO(model_path)
        print(f"✅ Model loaded successfully from {model_path}")
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return

    # Ensure output directory exists
    os.makedirs(output_path, exist_ok=True)

    # Run detection
    results = model.predict(
        source=processed_data_path,   # folder with processed images
        conf=0.5,                     # confidence threshold
        save=True,                    # save images with bounding boxes
        project=output_path,          # where to save results
        name='detections',            # subfolder name
        exist_ok=True
    )

    print("✅ Detection complete!")
    print(f"Results saved in: {os.path.join(output_path, 'detections')}")
