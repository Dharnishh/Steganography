# **Steganography-Based Secure Image Messaging System**

## **Project Overview**
This project is a **Python-based steganography tool** that allows users to securely hide secret messages within images. The tool uses pixel manipulation to embed messages into images and provides password protection for added security. The encrypted image can be shared, and only authorized users with the correct password can extract the hidden message.

---

## **Features**
- **Hide Secret Messages**: Embed text messages into images without visible changes.
- **Password Protection**: Secure the hidden message with a password.
- **Cross-Platform**: Works on Windows, macOS, and Linux.
- **User-Friendly**: Simple command-line interface for easy usage.

---

## **Technologies Used**
- **Programming Language**: Python
- **Libraries**:
  - OpenCV (`cv2`) for image processing.
  - OS and Subprocess for file handling and system operations.

---

## **How to Use**


### **Install Dependencies**
Make sure you have Python installed. Then, install the required libraries using pip:
```bash
pip install opencv-python
```

### **Run the Encryption Script**
1. Place the image you want to use in the same directory as the script.
2. Run the encryption script:
   ```bash
   python encrypt.py
   ```
3. Follow the prompts:
   - Enter the image name with an extension (e.g., `Dinesh.jpg`).
   - Enter the secret message you want to hide.
   - Enter a password for encryption.

4. The encrypted image will be saved as `Encryptedmsg.jpg`, and a metadata file (`metadata.txt`) will be created.

### **Run the Decryption Script**
1. Run the decryption script:
   ```bash
   python decrypt.py
   ```
2. Follow the prompts:
   - Enter the encrypted image name (e.g., `Encryptedmsg.jpg`).
   - Enter the password for decryption.

3. If the password is correct, the hidden message will be displayed.

---

## **Code Explanation**

### **Encryption Script (`encrypt.py`)**
1. **Input Validation**:
   - Checks if the image file exists and if the message/password is provided.
2. **Message Embedding**:
   - Uses pixel manipulation to embed the secret message into the image.
3. **Metadata Creation**:
   - Saves the password and message length in a `metadata.txt` file.
4. **Saving Encrypted Image**:
   - Saves the modified image as `Encryptedmsg.jpg`.

### **Decryption Script (`decrypt.py`)**
1. **Input Validation**:
   - Checks if the encrypted image and metadata file exist.
2. **Password Verification**:
   - Compares the entered password with the saved password.
3. **Message Extraction**:
   - Extracts the hidden message from the image using pixel manipulation.

---

## **File Structure**
```
steganography-project/
│
├── encrypt.py              # Script for embedding messages into images
├── decrypt.py              # Script for extracting messages from images
├── metadata.txt            # File containing password and message length
├── Encryptedmsg.jpg        # Encrypted image with a hidden message
├── README.md               # Project documentation
└── requirements.txt        # List of dependencies
```

---

## **Example Workflow**

### **Encryption**
1. Input:
   - Image: `Dinesh.jpg`
   - Message: `Hello World`
   - Password: `1234`
2. Output:
   - Encrypted image: `Encryptedmsg.jpg`
   - Metadata: `metadata.txt`

### **Decryption**
1. Input:
   - Encrypted image: `Encryptedmsg.jpg`
   - Password: `1234`
2. Output:
   - Decrypted message: `Hello World`

---

## **Future Scope**
- Add a **Graphical User Interface (GUI)** for better user experience.
- Implement **advanced encryption algorithms** (e.g., AES) for stronger security.
- Extend support for **video and audio steganography**.
- Develop a **web-based application** for wider accessibility.

---

## **Contributing**
Contributions are welcome! Feel free to open an issue or submit a pull request if you have any suggestions or improvements.
