# StegoSecure
# Image Steganography - Hide Secret Messages in Images

## 📌 Overview
This project employs advanced image-based steganography techniques to securely embed confidential messages within digital images by modifying pixel values. The resulting encrypted image remains visually indistinguishable from the original, ensuring secure and discreet communication without raising suspicion.

## ✨ Features
- 🔒 **Stealthy Data Hiding** – Stealthy Data Concealment – Embeds messages within pixel values with minimal perceptible distortion.
- 🎨 **RGB Channel Utilization** – Distributes hidden data across Red, Green, and Blue (RGB) channels for enhanced security.
- 🔑 **Password-Protected Decryption** – Implements password-protected decryption to ensure restricted access to hidden information.
- 📷 **Minimal Image Distortion** – Maintains the original visual quality of the image post-embedding.

## 🛠️ Technologies Used
- **Python** – Core programming language
- **OpenCV (cv2)** – Image processing library
- **NumPy** – Handling pixel data
- **OS** – File handling operations

## 🚀 Installation & Setup

1. Install dependencies:
   ```sh
   pip install opencv-python numpy
   ```
2. Place your image file (e.g., `picture.jpg`) in the project directory.
3. Run the encryption script:
    ```sh
    python encrypt.py
      ```



## 🔐 Usage
### 📝 Encryption
1. Run the encryption script:
   ```sh
   python encrypt.py
   ```
2. Enter the secret message and a password.
3. The message is embedded in the image, and `encryptedImage.jpg` is saved.

### 🔓 Decryption
1. Run the decryption script:
   ```sh
   python decrypt.py
   ```
2. Enter the correct password.
3. The hidden message is extracted and displayed.

## 👥 End Users
- **Cybersecurity Professionals** – Secure communication & data hiding.
- **Journalists & Whistleblowers** – Protect sensitive information.
- **Government & Intelligence Agencies** – Covert data transmission.
- **General Users** – Hide personal messages securely.

## 📌 Conclusion
This project provides a discreet and secure way to hide messages in images using steganography. By utilizing pixel manipulation and password protection, it ensures confidentiality without altering the image's appearance.

## 👨‍💻 Contributors
- **Nikitha George**
