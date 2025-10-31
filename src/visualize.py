import matplotlib.pyplot as plt
import cv2
import os

def show_results(result_folder, num_images=3):
    images = [img for img in os.listdir(result_folder) if img.endswith(('.jpg', '.png'))]
    for img_name in images[:num_images]:
        img_path = os.path.join(result_folder, img_name)
        img = cv2.imread(img_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(img_rgb)
        plt.title(img_name)
        plt.axis('off')
        plt.show()
