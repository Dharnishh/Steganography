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

### **Run the Script**
1. Place the image you want to use in the same directory as the script.
2. Run the encryption script:
   ```bash
   python stego.py
   ```
3. Follow the prompts:
   - Enter the image name with an extension (e.g., `Dinesh.jpg`).
   - Enter the secret message you want to hide.
   - Enter a password for encryption.

4. The encrypted image will be saved as `Encryptedmsg.jpg` will be created.

### **To Decrypt Data**

Do you want to decrypt the message? (y/n):
   - Enter y for execution of the script.
   - Enter n to end the process. 

If the password is correct, the hidden message will be displayed.

---

## **Code Explanation**

### **Script (`stego.py`)**
1. **Input Validation**:
   - Checks if the image file exists and if the message/password is provided.
2. **Message Embedding**:
   - Uses pixel manipulation to embed the secret message into the image.
3. **Saving Encrypted Image**:
   - Saves the modified image as `Encryptedmsg.jpg`.
4. **Input Validation**:
   - Checks if the decrypted image of the message is y/n.
5. **Password Verification**:
   - Compares the entered password with the saved password.
6. **Message Extraction**:
   - Extracts the hidden message from the image using pixel manipulation.

---

## **File Structure**
```
steganography-project/
│
├── stego.py                  
├── download.jpg             
├── Encryptedmsg.jpg          
└── README.md                 
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
3. Input:
   - Decrypted image: `Encryptedmsg.jpg`
   - Password: `1234`
4. Output:
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
