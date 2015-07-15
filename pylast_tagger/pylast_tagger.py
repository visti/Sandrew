import pylast
import tkinter
import re
import tkinter.filedialog
import tkinter.simpledialog
import random
from retrying import retry

global artist
global title
global itunes_main
global itunes_sub

# GUI Drawing + Focus settings

root = tkinter.Tk()
root.withdraw()
root.lift()
root.focus_force()

# Categorize genres
with open('main_genres.txt', 'r') as f:
	main_genres = [lines.strip() for lines in f]

with open('sub_genres.txt', 'r') as f:
	sub_genres = [lines.strip() for lines in f]



# read track list 
file_path = tkinter.filedialog.askopenfilename()

lines = open(file_path, 'r').readlines()

def split_track(song):
		stripped = [song.strip() for line in song]
		parts = stripped[0].split('|')
		global artist
		artist = parts[0]
		global title
		title = parts[1]

	

def search_lastfm(artist, title):
	try :
		track = network.get_track(artist, title)
		tags = track.get_top_tags()

		genre = []

		for topItem in tags:
			genre.append(topItem.item.get_name())

		global itunes_main
		global itunes_sub
		itunes_main = set([x.title() for x in genre]).intersection(main_genres)
		itunes_sub_raw = set([x.title() for x in genre]).intersection(sub_genres)
		itunes_sub = []
		for x in itunes_sub_raw:
			if x not in itunes_main:
				itunes_sub.append(x)
		final = str(track) +"|"+" ".join(itunes_main) +"|"+" ".join(itunes_sub) + "\n"
		print(final)
		writefile(final)
	
	except pylast.WSError:
		print(artist + " - " + title + "\n")




def writefile(final):
	with open("output.txt", 'a') as f:
		f.write(final)

# API Authentication

API_KEY = "8611a1f82dd20dc8ca8af7e5bc303ca9"
API_SECRET = "a2aa6b3434e4c96a05e1433bad60486f"
username = "visti"
password_hash = pylast.md5("hunter2")
network = pylast.LastFMNetwork(api_key = API_KEY, api_secret =
    API_SECRET, username = username, password_hash = password_hash)



# Main Loop


for song in lines:
	split_track(song)
	search_lastfm(artist, title)


#
