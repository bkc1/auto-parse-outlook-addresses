import re
import pyautogui as pya
import pyperclip
import time

#capture string from clipboard
def copy_clipboard():
    pya.hotkey('ctrl', 'c')
    time.sleep(.01) 
    return pyperclip.paste()

# double clicks on a position of the cursor
pya.doubleClick(pya.position())

outlook_copy = copy_clipboard()

# basic check for string format in clipboard
char = ["@", "<", ">"]
if all(x in outlook_copy for x in char):
  # strip full email contact name down to just an email address
  email = re.search(r"\<(.*?)\>", outlook_copy)
  # remove domain from email, reappend the '@'
  alias = ((email.group(1)).split('@')[0]) + '@'

  pyperclip.copy(alias)
  # Debug-only
  #msg = alias + ' has been copied to clipboard'
  #print(msg)
  pyperclip.paste()

else:
  error = "Error: " + outlook_copy + " was copied to the clipboard & doesn't appear to be a supported format."
  print(error)

