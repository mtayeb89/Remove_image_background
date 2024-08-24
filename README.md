# Remove_image_background
This Python script removes the background from an image using the rembg library and OpenCV.
Requirements

    Python 3.x
    rembg library
    OpenCV (cv2)

# Installation

Before running the script, make sure you have installed the required libraries:

bash

pip install rembg opencv-python

# How to Use

    Place your input image in the same directory as the script.
    Modify the input_path and output_path variables in the script to match your file names.
    Run the script. The output image with the background removed will be saved and displayed.

# Script Details

    input_path: Path to the input image.
    output_path: Path where the output image will be saved.
    cv2.imread: Reads the input image.
    remove: Removes the background from the input image.
    cv2.imwrite: Saves the output image.
    cv2.imshow: Displays the output image.

# Example

For an image named Icecreamcone.jpg, the script will generate Icecreamcone.png with the background removed.
License

This project is open-source and available for free under the MIT License.
