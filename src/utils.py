import os
import cv2

def load_images_from_folder(folder):
    images = []
    names = []
    for filename in os.listdir(folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(folder, filename)
            img = cv2.imread(img_path)
            if img is not None:
                images.append(img)
                names.append(filename)
    return images, names

def save_image(output_path, image):
    cv2.imwrite(output_path, image)
