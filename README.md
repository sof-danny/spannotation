# spannotation## Description of software
The package introduces a novel approach to image annotation and segmentation, requiring users to select just three key points on an image. These points define a triangular area representing the region of interest, which the algorithm then uses to generate a binary mask. This mask distinctly categorizes the image into two classes: drivable and non-drivable regions.

## Key applications of this package include:

1. Row Crop Management: In agricultural settings, such as cornfields, the package can segment row crops, identifying drivable paths for farm machinery and ensuring efficient navigation through the fields.
2. Off-Road Navigation: For off-road scenarios, like dirt tracks, the tool can demarcate navigable paths, assisting in the planning and navigation of off-road vehicles.
3. On-Road Navigation: In typical urban or rural roads, the package can be used to distinguish the actual road (drivable region) from its surroundings (non-drivable regions, including shoulders and adjacent land), aiding in basic navigation tasks.

This tool is particularly useful for researchers and practitioners in autonomous vehicle navigation, agricultural robotics, and geographic information systems (GIS), where accurate and efficient image segmentation is critical.

## Time comparison with dense annotation 

Spannotation saved average of **30 seconds** on one annotation of an average crop row or dirt road. 

**spannotation: 6.03 seconds** 

**Regular annotation: 40.39 seconds** 

## Installation
To install SPAnnotation, simply use pip: 

``` pip install spannotation ```

## Usage on Python code Editor
Here's a quick example of how to use spannotation if you are running from a typical code editor like jupyter, VSCode, etc:


# Step 1: Install spannotation
First, install the package using pip. Run the following command in a cell in your code editor:
``` pip install spannotation ```

# Step 2: Import the Package
In a new cell, import the MaskGenerator class from the package:

``` from Spannotation import MaskGenerator ```

# Step 3: Initialize the Generator
Create an instance of the MaskGenerator:
``` generator = MaskGenerator() ```

# Step 4: Process Images
Now, you can use the generator to process an image or a folder of images.

To process a single image:

``` generator.process_image('path/to/your/image.jpg', 'path/to/save/mask') ```

To process all images in a folder:

``` generator.process_folder('path/to/your/images', 'path/to/save/masks') ```

Replace 'path/to/your/image.jpg', 'path/to/your/images', and 'path/to/save/masks' with the actual paths on your system.


## Usage on Command line / Terminal
Here's a quick example of how to use spannotation if you are running from command line or terminal:


### Installation

Ensure `Spannotation` is installed:

```
pip install spannotation
```
## Step 1: Run the tool
Open your terminal or command prompt.
Run Spannotation by typing:
``` spannotation ```

## Step 2: Choose operation mode
Enter 1 to process a single image.
Enter 2 to process all images in a folder.

### For a Single Image
Enter the full path to the image when prompted.
Specify the path to save the mask.
The image will open in a window. Click to select three points defining the drivable area.
The mask will be generated and saved in the specified directory.


### For Images in a Folder
Enter the full path to the folder containing the images.
Specify the save path for the masks.
For each image in the folder, select three points. Masks will be saved automatically.




## Examples  
### Example 1: Row-Crop Segmentation
![This shows the original image of a crop row](https://github.com/sof-danny/spannotation/blob/master/sample_images/row_crop.png)
![This image shows the mask generated using spannotation](https://github.com/sof-danny/spannotation/blob/master/sample_images/row_crop_mask.png)


### Example 2: Off-Road Navigation
![This shows the original image of a dirt road](https://github.com/sof-danny/spannotation/blob/master/sample_images/dir_road.png)
![This image shows the mask generated using spannotation](https://github.com/sof-danny/spannotation/blob/master/sample_images/dirt_road_mask.png)


## Performing deep learning training using generated mask 

Training performance of 1030 images/masks used to train a U-Net model:

![Training performances](https://github.com/sof-danny/spannotation/blob/master/sample_images/training_result.png)

Sample semantic segmentation from the model trained with the data:

![Sample segmentation](https://github.com/sof-danny/spannotation/blob/master/sample_images/sample_segmentation.png)


## Contributing
Contributions to spannotation are welcome! reach out to [Folorunsho Samuel](mailto:folorunshosamuel001@gmail.com)


## License
spannotation is released under the [MIT License](https://opensource.org/license/mit).

## Project details
Please check the gitup page : [Github](https://github.com/sof-danny/spannotation)


## Contact Info
Please reach out via: 

[LinkedIn](https://www.linkedin.com/in/samuelofolorunsho/)

[Email](mailto:folorunshosamuel001@gmail.com)


## Citation

If you use spannotation in your research or project, please consider citing it. Here is an example citation format you can use:

@misc{spannotation,
author = {Samuel Folorunsho},
title = {spannotation: Efficient Image Segmentation for Navigation Tasks},
year = {2024},
publisher = {GitHub},
journal = {GitHub repository},
howpublished = {https://github.com/sof-danny/spannotation}
}



