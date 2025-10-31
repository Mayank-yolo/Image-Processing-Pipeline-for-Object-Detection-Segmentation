from ultralytics import YOLO
import os

def segment_objects(model_path, input_folder, output_folder):
    """
    Runs object segmentation using YOLOv8 model (task='segment').
    Saves output images with segmentation masks drawn.
    """
    print("🧠 Starting segmentation...")

    model = YOLO(model_path)
    os.makedirs(output_folder, exist_ok=True)

    # Run segmentation inference
    results = model.predict(
        source=input_folder,
        save=True,
        project=output_folder,
        name="segmentation",
        task="segment",
        exist_ok=True
    )

    print(f"✅ Segmentation complete! Results saved to: {output_folder}/segmentation")
    return results
