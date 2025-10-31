# src/preprocess.py

import cv2
import os
import numpy as np

def preprocess_image(image):
    """
    Preprocess a single image:
    - Resize to 640x640
    - Apply Gaussian blur
    - Normalize pixel values
    - Convert to grayscale (optional)
    """
    try:
        # Resize to standard size
        resized = cv2.resize(image, (640, 640))

        # Optional: apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(resized, (5, 5), 0)

        # Normalize pixel values to range [0, 1]
        normalized = blurred / 255.0

        # Optional: convert to grayscale (comment out if you want RGB)
        gray = cv2.cvtColor((normalized * 255).astype(np.uint8), cv2.COLOR_BGR2GRAY)
        gray_rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)  # convert back to RGB for YOLO compatibility

        return gray_rgb

    except Exception as e:
        print(f"❌ Error preprocessing image: {e}")
        return image


def preprocess_images(input_folder, output_folder):
    """
    Batch preprocess all images in a folder.
    """
    os.makedirs(output_folder, exist_ok=True)
    count = 0

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(input_folder, filename)
            img = cv2.imread(image_path)
            if img is None:
                print(f"⚠️ Skipping unreadable image: {filename}")
                continue

            processed = preprocess_image(img)
            save_path = os.path.join(output_folder, filename)
            cv2.imwrite(save_path, cv2.cvtColor(processed, cv2.COLOR_RGB2BGR))
            count += 1

    print(f"✅ Preprocessed {count} images and saved to {output_folder}")
