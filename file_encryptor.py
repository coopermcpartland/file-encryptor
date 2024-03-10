import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os

KEY_FILE = "key.key"

def generate_key():
    """Generate a key and save it to a file."""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():
    """Load the key from the file."""
    if not os.path.exists(KEY_FILE):
        messagebox.showerror("Error", "Key file does not exist. Please generate a key first.")
        return None

    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

def encrypt_file():
    """Encrypt a file."""
    key = load_key()
    if key is None:
        return

    filename = filedialog.askopenfilename(title="Select File to Encrypt")
    if not filename:
        return

    fernet = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)

    save_filename = filedialog.asksaveasfilename(title="Save Encrypted File As", defaultextension=".encrypted")
    if not save_filename:
        return

    with open(save_filename, "wb") as file:
        file.write(encrypted_data)
    messagebox.showinfo("Success", "File encrypted successfully.")

def decrypt_file():
    """Decrypt an encrypted file."""
    key = load_key()
    if key is None:
        return

    filename = filedialog.askopenfilename(title="Select File to Decrypt")
    if not filename:
        return

    if not filename.endswith(".encrypted"):
        messagebox.showerror("Error", "Selected file is not an encrypted file.")
        return

    fernet = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception as e:
        messagebox.showerror("Error", "Failed to decrypt file. Ensure the correct key is used.")
        return

    save_filename = filedialog.asksaveasfilename(title="Save Decrypted File As")
    if not save_filename:
        return

    with open(save_filename, "wb") as file:
        file.write(decrypted_data)
    messagebox.showinfo("Success", "File decrypted successfully.")

def main():
    """Main function to create the GUI."""
    window = tk.Tk()
    window.title("File Encryptor")

    # Generate Key Button
    btn_generate_key = tk.Button(window, text="Generate Key", command=generate_key)
    btn_generate_key.pack(pady=10)

    # Encrypt File Button
    btn_encrypt = tk.Button(window, text="Encrypt File", command=encrypt_file)
    btn_encrypt.pack(pady=10)

    # Decrypt File Button
    btn_decrypt = tk.Button(window, text="Decrypt File", command=decrypt_file)
    btn_decrypt.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
