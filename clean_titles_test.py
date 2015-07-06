#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter
import tkFileDialog
import tkSimpleDialog
import re
import time
import datetime
import os

# Pattern to search for

messy_title_pat = re.compile(r', (The|A|An)$')

# Backup old log-file

if os.path.isfile('logfile2.txt'):
    os.remove('logfile2.txt')
if os.path.isfile('logfile.txt'):
    os.rename('logfile.txt', 'logfile2.txt')

# Options

noncorrectlog = 0

# GUI Drawing + Focus settings

root = Tkinter.Tk()
root.withdraw()
root.lift()
root.focus_force()

# Choose Input/Output Files

file_path = tkFileDialog.askopenfilename()
clean_path = tkSimpleDialog.askstring('Gem renset fil',
        'Indtast filnavn', initialvalue=file_path[:-4] + 'Clean.txt')
lines = open(file_path, 'r').readlines()


def logfile(song_title):
    with open('logfile.txt', 'a') as f:
        ts = time.time()
        logtime = \
            datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        f.write(logtime + ' - ' + song_title)


def add_lines(song_title):
    with open(clean_path, 'a') as f:
        f.write(song_title)


def clean_title(song_title):
    match = messy_title_pat.search(song_title)
    if match:
        print 'RETTET: ' + '"' + song_title.strip() + '"'
        logfile(song_title)
        return match.group(1) + ' ' + song_title[:match.start()] + '\n'
    else:

        # If noncorrect-log is on, also output non-corrected filenames to log file

        if noncorrectlog == 1:
            print 'IKKE RETTET: ' + '"' + song_title.strip() + '"'
            logfile('IKKE RETTET: ' + song_title)
            return song_title
        else:
            return song_title


### MAIN LOOP ###

for song_title in lines:
    add_lines(clean_title(song_title))

### MAIN LOOP ###
