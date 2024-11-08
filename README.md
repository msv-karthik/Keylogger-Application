# Keylogger-Application

This project is a basic **Keylogger** built with **Python**, utilizing the **tkinter** library for a graphical interface and **pynput** for capturing keyboard events. The program records key presses and releases, saving this data in both a **JSON** and a **text** file.

## Features

- **Keyboard Logging**: Records every key press and release.
- **JSON and Text Logging**: Saves logs in both `log.json` (JSON format) and `log.txt` (text format) for easy access.
- **Graphical Interface**: A simple Tkinter-based GUI to start the keylogger.
- **Exit Condition**: Pressing the 'Esc' key stops the keylogger.

## How It Works

1. **GUI Setup**: A Tkinter window with a "Start Keylogger" button is created.
2. **Key Press and Release Capture**: When the keylogger starts, it listens for both key press and key release events.
3. Each key event is appended to a list (`key_list`) and saved in JSON format to `log.json`.
4. Key strokes are also stored as a string (`key_strokes`) and written to `log.txt`.
5. **Exit Condition**: Pressing 'Esc' ends the keylogger session.

## Program Files

- **`log.json`**: Records key presses and releases in JSON format.
- **`log.txt`**: Stores all key strokes as a continuous string.

## Code Structure

### 1. **GUI Initialization**: 
   Tkinter is used to create a button that initiates the keylogger.

### 2. **File Management**:
   - **`update_txt_file()`**: Updates `log.txt` with key strokes.
   - **`update_json_file()`**: Updates `log.json` with detailed key press/release data.

### 3. **Keyboard Listener**: 
   Uses the **pynput** library's Listener to capture key events.
   - **`on_press()`**: Appends pressed keys to `key_list`.
   - **`on_release()`**: Appends released keys to `key_list` and updates `log.txt`.

## Installation and Setup

1. Install the required libraries:

    ```bash
    pip install tkinter pynput
    ```

2. Copy the code into a Python file, e.g., `keylogger.py`.

3. Run the script:

    ```bash
    python keylogger.py
    ```

## Usage

- **Start Keylogger**: Click "Start Keylogger" in the GUI to begin capturing key events.
- **Stopping the Keylogger**: Press the 'Esc' key to end logging.
