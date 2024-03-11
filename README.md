# File Encryptor

![File Encryptor](screenshots/gui.jpg)

File Encryptor is a Python tool for securely encrypting and decrypting files using the Fernet symmetric encryption algorithm from the `cryptography` library.

## Features
- Generate encryption keys securely.
- Encrypt files with a chosen key.
- Decrypt encrypted files with the correct key.
- User-friendly GUI for easy file selection.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/coopermcpartland/file-encryptor.git
   cd file-encryptor

2. Install Dependencies:
   ```bash
   pip install -r requirements.txt

## Usage
1. Run the script:
   ```bash
   python file_encryptor.py

2. GUI will open with options to:
Generate Key
Encrypt File
Decrypt File
Choose files and save locations with file dialogs.

## Security
Uses Fernet symmetric encryption for strong security.
Key management ensures keys are securely generated and stored.
Robust error handling prevents unauthorized access.

## Contributing
Contributions are welcome! Fork the repository and submit pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for details
