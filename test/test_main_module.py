import unittest
import numpy as np
from Spannotation.mask_generator import MaskGenerator

class TestMaskGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = MaskGenerator()

    def test_generate_mask(self):
        
        # Create a mock image 
        mock_image = np.zeros((3, 3, 3), dtype=np.uint8)

        # Define points that form a triangle within the image
        points = [(0, 1), (2, 0), (1, 2)]

        # Generate the mask
        mask = self.generator.generate_mask(mock_image, points)

        expected_mask = np.array([
            [1, 1, 1],
            [0, 1, 0],
            [0, 0, 0]
        ], dtype=np.uint8)

        
        np.testing.assert_array_equal(mask, expected_mask)

if __name__ == '__main__':
    unittest.main()




