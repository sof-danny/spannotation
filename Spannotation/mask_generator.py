import cv2
import numpy as np
import os
import glob

class MaskGenerator:
    def __init__(self):
        self.points = []
        self.image = None
        self.mask_generated = False

    def click_event(self, event, x, y, flags, param):
        """Handles mouse click events to select points on the image."""
        if event == cv2.EVENT_LBUTTONDOWN:
            if len(self.points) < 3:
                self.points.append((x, y))
                cv2.circle(self.image, (x, y), 5, (0, 255, 0), -1)
                cv2.imshow('image', self.image)

            if len(self.points) == 3 and not self.mask_generated:
                mask = self.generate_mask(self.image, self.points)
                cv2.imshow('mask', mask)
                self.mask_generated = True

    @staticmethod
    def generate_mask(image, points):
        """Generates a binary mask based on the selected points."""
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        cv2.fillPoly(mask, [np.array(points)], 255)
        return mask

    def process_image(self, image_path, save_path):
        """Processes a single image for mask generation."""
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise ValueError("Could not read the image.")
        self.points = []
        self.mask_generated = False

        cv2.imshow('image', self.image)
        cv2.setMouseCallback('image', self.click_event)
        cv2.waitKey(0)
        cv2.destroyAllWindows()  # Close the image window

        if self.mask_generated:
            mask = self.generate_mask(self.image, self.points)
            base_name = os.path.basename(image_path)
            cv2.imwrite(os.path.join(save_path, base_name), mask)

    def process_folder(self, folder_path, save_path):
        """Processes all images in a given folder."""
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        for image_file in glob.glob(os.path.join(folder_path, '*')):
            try:
                self.process_image(image_file, save_path)
            except ValueError as e:
                print(f"Error processing {image_file}: {e}")
