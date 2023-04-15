import sys
import pyperclip
from random import randint

IGNORED_CHARS = [34, 42, 44, 46, 58, 59, 60, 62, 94, 96, 123, 124, 125] + [ord(item) for item in sys.argv[2:]]
pw_len = sys.argv[1] if len(sys.argv) > 0 else 35
pw = ""
i = 0
while i < pw_len:
    charcode = randint(33, 126)
    if charcode not in IGNORED_CHARS:
        pw += chr(charcode)
        i += 1
pyperclip.copy(pw)
print(f'\n>>> I made this for you! ---> {pw}')
