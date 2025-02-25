import cv2

# Load the encrypted image
img = cv2.imread("encryptedImage.jpg")

# Extract message length from the first pixel
msg_length = img[0, 0][0] * 256 + img[0, 0][1]  # Extract length from (R, G)

# Character mapping (ASCII to character)
c = {i: chr(i) for i in range(255)}

# Password verification
stored_password = input("Enter passcode for decryption: ")

# Decrypt the message
message = ""
n, m, z = 0, 1, 0  # Start from (0,1) at Red channel

for _ in range(msg_length):
    message += c[int(img[n, m, z])]  # Convert back to character
    z = (z + 1) % 3  # Cycle through RGB
    if z == 0:
        m += 1  # Move to next pixel
        if m >= img.shape[1]:  # If column overflow, move to next row
            m = 0
            n += 1

print("Decryption successful!")
print("Decrypted message:", message)
