This Python script removes the background from an image using the rembg library and displays the processed image using matplotlib.
# Requirements

    Python 3.x
    rembg library
    opencv-python library
    matplotlib library

# Installation

Before running the script, make sure you have installed the required libraries. You can install them using pip:

bash

pip install rembg opencv-python matplotlib

# How to Use

    Place your input image in the same directory as the script.
    Modify the input_path and output_path variables in the script to match your file names.
    Run the script. The output image with the background removed will be saved to the specified path and displayed.

Example:

    Input Image: Icecreamcone.jpg
    Output Image: Icecreamcone.png

# Running the Script:

    Open a terminal or command prompt in the directory where your script is located.

    Run the script using Python:

    bash

    python Remove_background.py

# What the Script Does:

    Input Image Path: The path to the image you want to process.
    Output Image Path: The path where the processed image will be saved.
    Background Removal: The script uses the rembg library to remove the background from the input image.
    Save and Display: The processed image is saved to the specified output path and displayed using matplotlib.

# Troubleshooting
Common Errors:

    No Module Named matplotlib: Install matplotlib using pip install matplotlib.
    OpenCV Error on cv2.imshow: If you're using a headless environment, you can replace cv2.imshow with matplotlib to display images.

License

This project is open-source and available under the MIT License.
