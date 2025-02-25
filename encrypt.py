import cv2
import os
import numpy as np

# Load the image
img = cv2.imread("mypic.jpg")  # Replace with your image path

# Take user input
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Character-to-ASCII mapping
d = {chr(i): i for i in range(255)}

# Store message length in the first two pixels
msg_length = len(msg)
img[0, 0] = [msg_length // 256, msg_length % 256, 0]  # (R, G) store length

# Encoding message into the image
n, m, z = 0, 1, 0  # Start from (0,1) at Red channel

for char in msg:
    img[n, m, z] = np.uint8(d[char])  # Store ASCII value
    z = (z + 1) % 3  # Cycle through RGB
    if z == 0:
        m += 1  # Move to next pixel
        if m >= img.shape[1]:  # If column overflow, move to next row
            m = 0
            n += 1

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
print("Message encrypted successfully into 'encryptedImage.jpg'.")
os.system("start encryptedImage.jpg")  # Open image (Windows)
