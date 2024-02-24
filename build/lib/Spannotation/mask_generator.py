import cv2
import numpy as np
import os
import glob


class MaskGenerator:
    def __init__(self):
        self.points = []
        self.image = None
        self.mask_generated = False
        self.window_name = 'Image Mask Generator'  


    def click_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            if len(self.points) < 3:  
                self.points.append((x, y))
                cv2.circle(self.image, (x, y), 5, (0, 255, 0), -1)
                cv2.imshow('image', self.image)

            if len(self.points) == 3 and not self.mask_generated:
                mask = self.generate_mask(self.points)
                cv2.imshow('mask', mask)
                self.mask_generated = True
                self.save_mask(mask, param['save_path'], param['image_path'])
                cv2.waitKey(500)  
                cv2.destroyAllWindows()
                cv2.waitKey(1)  

    def generate_mask(self, points):
        mask = np.zeros(self.image.shape[:2], dtype=np.uint8)
        cv2.fillPoly(mask, [np.array(points)], 255)
        return mask

    def save_mask(self, mask, save_path, image_path):
        base_name = os.path.basename(image_path)
        save_file = os.path.join(save_path, base_name)
        cv2.imwrite(save_file, mask)
        print(f"Mask saved to {save_file}")
        
   
    def process_image(self, image_path, save_path):
        self.image = cv2.imread(image_path)
        self.points = []
        self.mask_generated = False

        cv2.imshow('image', self.image)
        cv2.setMouseCallback('image', self.click_event, param={'image_path': image_path, 'save_path': save_path})
        
        while not self.mask_generated:
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break

        cv2.destroyAllWindows()
        cv2.waitKey(1)  

    def process_folder(self, folder_path, save_path):
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        for image_file in glob.glob(os.path.join(folder_path, '*')):
            self.process_image(image_file, save_path)
