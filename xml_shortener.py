#-*- coding: UTF-8 -*-
# A script to find XML fields exceeding an 80 character limit and shorten them.
# Uses a tkinter file selection dialog


import xml.etree.cElementTree as ET
import itertools
import tkinter
import tkinter.filedialog
import tkinter.simpledialog
from tkinter.simpledialog import Dialog
from tkinter.simpledialog import Toplevel
from tkinter.simpledialog import Label
import winsound
import os

username = os.getlogin()

# GUI Drawing + Focus settings
tkroot = tkinter.Tk()
tkroot.withdraw()
tkroot.lift()
tkroot.focus_force()


# choose original file
original_file = tkinter.filedialog.askopenfilename(
    title="Choose File:", initialdir=os.curdir)

output_file = original_file[:-4] + '_fixed.xml'

# create tree from XML file
tree = ET.parse(original_file)
root = tree.getroot()

# iterate through the 3 elements:
field_list = ["MAIN-ARTIST-NAME-COLLECTING-SOCIETY",
                  "RECORDING-TITLE-COLLECTING-SOCIETY",
                  "LABEL"]

def working_message(username):
    os.system('cls')
    print("\n" * 10)
    print("-" * 120)
    print("\n")
    print("XML Shortening Script".center(120))
    print("Working..".center(120))
    print("\n")
    print("running for user: \n".center(120))
    print(username.center(120))
    print("-" * 120)
    print("\n")
    
working_message(username)

for i in field_list:
    for element in root.iter(i):
        if len(element.text) > 80:
            element.text = element.text[:80]

tree = ET.ElementTree(root)


# write corrected file to disk
tree.write(open(output_file, 'wb'), encoding="utf-8", xml_declaration=True)

# Completion message
winsound.MessageBeep(1)
tkinter.messagebox.showinfo("Done!",  "Created file: \n" + output_file + ".")

