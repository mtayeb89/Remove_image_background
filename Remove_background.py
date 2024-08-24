# Import the remove function from the rembg library for background removal
from rembg import remove

# Import the OpenCV library for image processing tasks
import cv2

# Import matplotlib for displaying images
import matplotlib.pyplot as plt

# Define the path to the input image file
input_path = 'Icecreamcone.jpg'

# Define the path where the output image (with background removed) will be saved
output_path = 'Icecreamcone.png'

# Read the input image from the specified path
input_image = cv2.imread(input_path)

# Remove the background from the input image using the remove function
output_image = remove(input_image)

# Save the output image (with background removed) to the specified path
cv2.imwrite(output_path, output_image)

# Convert the image from BGR (OpenCV default) to RGB (for correct display in matplotlib)
output_image_rgb = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)

# Display the output image using matplotlib
plt.imshow(output_image_rgb)
plt.title('Output Image')
plt.axis('off')  # Turn off axis numbers and ticks
plt.show()

