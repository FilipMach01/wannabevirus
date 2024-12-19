import subprocess
import sys
import pyautogui
import time

def macro_typing():
    # macro spam of starting the same program in consolestart
    pyautogui.typewrite("start")
    pyautogui.press("enter")
def open_command_prompt():
    try:
        # Open command prompt
        subprocess.Popen(['cmd.exe', '/k'], creationflags=subprocess.CREATE_NEW_CONSOLE)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    open_command_prompt()
    time.sleep(0.4)
    print()
    while True:
        macro_typing()
        open_command_prompt()


