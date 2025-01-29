# Simple Facebook Messenger Chat Deletion Bot

## Overview
This is a very simple bot created to automate the deletion of Facebook Messenger chats on the URL [https://www.facebook.com/messages](https://www.facebook.com/messages). Since Messenger does not provide an option to delete all messages at once, this bot was designed to speed up the process.

## How It Works
The bot primarily relies on screen positions to interact with the Messenger interface. It was created with the sole purpose of solving this problem as quickly as possible, without any advanced automation frameworks.

## Requirements
Install the necessary dependencies:

```sh
pip install -r requirements.txt
```

Contents of `requirements.txt`:
```plaintext
keyboard==0.13.5
MouseInfo==0.1.3
opencv-python==4.11.0.86
pillow==9.5.0
PyAutoGUI==0.9.54
pynput==1.7.7
```

## Usage
1. Open the Facebook Messenger page: [https://www.facebook.com/messages](https://www.facebook.com/messages).
2. Position the browser window properly on your screen.
3. Run the script:
   ```sh
   python delete_message_bot_position.py
   ```
4. Press `ESC` at any time to stop the script.

## Files
- `delete_message_bot_position.py`: Main script for automating chat deletion.
- `delete_option.png`: Image used for detecting the "Delete Chat" button.
- `tela_teste.png`: Debug screenshot to ensure the UI elements are being captured correctly.
- `position.py`: A helper script to capture mouse positions on the screen. It records positions as you click the mouse or press the `P` key.
- `requirements.txt`: Lists the Python dependencies for this project.

## Disclaimer
This bot is a quick and basic solution for personal use. Automating actions on third-party platforms like Facebook may violate their terms of service. Use responsibly.

---

Created by [Arthur Graf](https://github.com/arthurmgraf).

