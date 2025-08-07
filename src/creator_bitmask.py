import cv2 as cv
import numpy as np

# Define image dimensions (height, width)
height = 1064 // 2  # 532
width = 768 // 2    # 384

# Create a black image (bitmask)
mask = np.zeros((height, width), dtype=np.uint8)

# Draw a white circle in the center
diameter = 100
radius = diameter // 2
center = (width // 2, height // 2)
cv.circle(mask, center, radius, 255, -1)  # 255 for white, -1 to fill

# Save the image as JPEG
output_path = 'src/circle_bitmask.jpg'
cv.imwrite(output_path, mask)

# Display the mask inline
import matplotlib.pyplot as plt
plt.imshow(mask, cmap='gray')
plt.title('Circular Bitmask')
plt.axis('off')
plt.show()

