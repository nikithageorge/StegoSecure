# StegoSecure
# Image Steganography - Hide Secret Messages in Images

## 📌 Overview
This project implements image-based steganography, allowing users to securely embed secret messages within an image by modifying pixel values. The modified image appears unchanged, ensuring discreet communication.

## ✨ Features
- 🔒 **Stealthy Data Hiding** – Encodes messages within pixel values without visible distortion.
- 🎨 **RGB Channel Utilization** – Spreads the message across Red, Green, and Blue channels.
- 🔑 **Password-Protected Decryption** – Ensures only authorized users can retrieve the hidden message.
- 📷 **Minimal Image Distortion** – Keeps the image visually identical after encryption.

## 🛠️ Technologies Used
- **Python** – Core programming language
- **OpenCV (cv2)** – Image processing library
- **NumPy** – Handling pixel data
- **OS** – File handling operations

## 🚀 Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/image-steganography.git
   cd image-steganography
   ```
2. Install dependencies:
   ```sh
   pip install opencv-python numpy
   ```
3. Place your image file (e.g., `mypic.jpg`) in the project directory.

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
