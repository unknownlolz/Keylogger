MADE BY DARSH
---

# Keylogger

## Overview

This Python script is a simple keylogger designed to record alphanumeric characters, spaces, and common punctuation marks while ignoring other special keys. It uses the `pynput` library to monitor keyboard inputs and logs them to a file.

## How It Works

- The script listens for keyboard events using the `pynput` library.
- It checks each pressed key to determine if it's a printable character (alphanumeric, punctuation, etc.).
- If the key is printable, it's logged to a file named `keylog.txt`.
- The script continues running until the `Esc` key is pressed, at which point it stops.

## Usage

1. **Installation**

    - Ensure you have Python 3 installed on your system.
    - Install the required `pynput` library by running:
  
      pip install pynput  

2. **Running the Keylogger**

    - Navigate to the directory containing the `keylogger.py` script.
    - Run the script using the following command:

      python3 keylogger.py


3. **Stopping the Keylogger**

    - To stop the keylogger, press the `Esc` key. This will terminate the script and stop logging keystrokes.
    - Alternatively, you can manually terminate the script by closing the terminal or using the appropriate system command.

4. **Accessing the Logs**

    - The keystrokes are logged to a file named `keylog.txt`, which will be created in the same directory as the script.
    - You can open this file using any text editor to view the logged keystrokes.

## Permissions

- **Accessibility Permissions**: On macOS, you may need to grant accessibility permissions to your terminal and Python interpreter to allow the script to capture keystrokes. Follow the instructions in your system preferences to grant these permissions.

## Legal and Ethical Considerations

- **Ethical Use**: Use this script responsibly and ethically. Only run it on devices you own or have explicit permission to monitor.
- **Privacy**: Be aware of privacy concerns when logging keystrokes. Ensure you have consent from users before monitoring their keyboard input.
- **Legal Compliance**: Understand and comply with the laws and regulations in your jurisdiction regarding the use of keylogging software.

## Disclaimer

This script is provided for educational purposes only. The author and contributors are not responsible for any misuse of this software.

---

Feel free to customize this README according to your needs or to include any additional information. Make sure to include any relevant legal disclaimers and ethical considerations.
