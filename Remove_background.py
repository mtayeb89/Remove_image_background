# Import the remove function from the rembg library for background removal
from rembg import remove

# Import the OpenCV library for image processing tasks
import cv2

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

# Display the output image in a window
cv2.imshow(output_path, output_image)

# Wait indefinitely for a key press; close the window if 'q' is pressed
if cv2.waitKey(0) & 0xFF == ord('q'):
    # Close the currently opened image window
    cv2.close()

    # Destroy all windows created by OpenCV to free up resources
    cv2.destroyAllWindows()
