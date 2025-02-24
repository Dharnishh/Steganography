import cv2
import os
import subprocess

# Function to validate user inputs
def validate_input(img_path, msg, password):
    """
    Validates the input provided by the user.
    Returns an error message if any input is invalid.
    """
    if not os.path.exists(img_path):
        return "Error: Image file not found! Please check the file name and extension."
    if not msg:
        return "Error: Secret message cannot be empty!"
    if not password:
        return "Error: Password cannot be empty!"
    return None  # No errors

# Function to embed the secret message into the image
def embed_message(img, msg):
    """
    Embeds the secret message into the image using pixel manipulation.
    """
    d = {chr(i): i for i in range(255)}  # Dictionary to map characters to ASCII values
    m, n, z = 0, 0, 0  # Variables to track pixel positions

    # Embed the message into the image
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]  # Modify pixel values
        n += 1
        m += 1
        z = (z + 1) % 3  # Cycle through RGB channels

    return img

# Function to extract the secret message from the image
def extract_message(img, msg_length):
    """
    Extracts the secret message from the image using pixel manipulation.
    """
    c = {i: chr(i) for i in range(255)}  # Dictionary to map ASCII values to characters
    m, n, z = 0, 0, 0  # Variables to track pixel positions
    message = ""  # Variable to store the extracted message

    # Extract the message from the image
    for _ in range(msg_length):
        message += c[img[n, m, z]]  # Retrieve character from pixel values
        n += 1
        m += 1
        z = (z + 1) % 3  # Cycle through RGB channels

    return message

# Main program
if __name__ == "__main__":
    # Step 1: Input image name with extension
    img_name = input("Enter the image name with extension (e.g., Dinesh.jpg): ").strip()
    img_path = os.path.join(os.getcwd(), img_name)  # Get full path of the image

    # Step 2: Input secret message
    msg = input("Enter the secret message: ").strip()

    # Step 3: Input password
    password = input("Enter a password for encryption: ").strip()

    # Step 4: Validate inputs
    error = validate_input(img_path, msg, password)
    if error:
        print(error)
        exit()

    # Step 5: Load the image
    img = cv2.imread(img_path)
    if img is None:
        print("Error: Unable to load image. Please check the file format.")
        exit()

    # Step 6: Embed the message into the image
    encrypted_img = embed_message(img.copy(), msg)
    encrypted_img_path = "Encryptedmsg.jpg"
    cv2.imwrite(encrypted_img_path, encrypted_img)
    print(f"Message embedded and saved as {encrypted_img_path}")

    # Step 7: Open the encrypted image (cross-platform compatibility)
    if os.name == "nt":  # Windows
        subprocess.run(["start", encrypted_img_path], shell=True)
    elif os.name == "posix":  # macOS or Linux
        subprocess.run(["open", encrypted_img_path])
    else:
        print(f"Encrypted image saved at: {encrypted_img_path}")

    # Step 8: Decryption
    decrypt_choice = input("Do you want to decrypt the message? (y/n): ").strip().lower()
    if decrypt_choice == 'y':
        pas = input("Enter the password for decryption: ").strip()

        # Verify the password
        if password == pas:
            # Extract the message
            decrypted_msg = extract_message(encrypted_img, len(msg))
            print("Decrypted message:", decrypted_msg)
        else:
            print("Error: Incorrect password!")