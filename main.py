import os
import cv2
from src.utils import load_images_from_folder
from src.preprocess import preprocess_image
from src.detect import detect_objects
from src.visualize import show_results
from src.segment import segment_objects


if __name__ == "__main__":
    print("🚀 Starting Image Processing Pipeline...")

    # Define key paths
    raw_data_path = "data/raw"
    processed_data_path = "data/processed"
    model_path = "models/yolov8n.pt"
    detection_output = "results/detections"
    segmentation_output = "results/reports"

    # Step 1: Load raw images
    images, names = load_images_from_folder(raw_data_path)
    if not images:
        print(f"❌ No images found in {raw_data_path}")
        exit()
    print(f"📥 Loaded {len(images)} images from {raw_data_path}")

    # Step 2: Preprocess and save
    os.makedirs(processed_data_path, exist_ok=True)
    for img, name in zip(images, names):
        processed = preprocess_image(img)
        save_path = os.path.join(processed_data_path, name)
        cv2.imwrite(save_path, cv2.cvtColor(processed, cv2.COLOR_RGB2BGR))
    print("✅ Preprocessing complete and saved to:", processed_data_path)

    # Step 3: Object Detection
    detect_objects(model_path, processed_data_path, "results")
    
    # Step 4: Object Segmentation
    segment_objects(model_path, processed_data_path, segmentation_output)

    # Step 5: Visualize Detection Results
    show_results(detection_output)

    print("🏁 Pipeline finished successfully!")
