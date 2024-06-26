import pyperclip
import webbrowser
from pynput import keyboard

# Dictionary to keep track of the state of each key
key_state = {"ctrl": False, "c_pressed": False}


def on_press(key):
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        key_state["ctrl"] = True
    elif key == keyboard.KeyCode.from_char("c"):
        if key_state["ctrl"]:
            key_state["c_pressed"] = True
    elif key == keyboard.KeyCode.from_char("d"):
        if key_state["ctrl"] and key_state["c_pressed"]:
            open_deepl_translator()
            key_state["c_pressed"] = False  # Reset the state after action


def on_release(key):
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        key_state["ctrl"] = False
        key_state["c_pressed"] = False  # Reset the state if 'ctrl' is released


# Function to open the URL with the clipboard content
def open_deepl_translator():
    print("Opening DeepL translator...")
    text = pyperclip.paste()
    url = f"https://www.deepl.com/translator#de/en/{text}"
    webbrowser.get("firefox")
    webbrowser.open(url)


if __name__ == "__main__":
    print("Listening for Ctrl + C + D...")
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    ) as listener:
        listener.join()

# sudo cp ./deepl_translation.service ~/systemd/.config/systemd/user/translation.service

# sudo systemctl --user daemon-reload
# sudo systemctl --user start translation.service
# sudo systemctl --user status translation.service
# journalctl --user -u translation.service -b
