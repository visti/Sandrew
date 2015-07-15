import pylast
import tkinter
import re
import tkinter.filedialog
import tkinter.simpledialog

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


with open(file_path, 'r') as f:
	lines = [line.strip() for line in f]
	parts = lines[0].split('|')
	artist = parts[0]
	title = parts[1]



# API Authentication

API_KEY = "8611a1f82dd20dc8ca8af7e5bc303ca9"
API_SECRET = "a2aa6b3434e4c96a05e1433bad60486f"
username = "visti"
password_hash = pylast.md5("penbird")
network = pylast.LastFMNetwork(api_key = API_KEY, api_secret =
    API_SECRET, username = username, password_hash = password_hash)



# Main Loop

track = network.get_track(artist, title)

tags = track.get_top_tags()

genre = []

for topItem in tags:
    genre.append(topItem.item.get_name())

itunes_main = set([x.title() for x in genre]).intersection(main_genres)
itunes_sub = set([x.title() for x in genre]).intersection(sub_genres)

for x in itunes_main:
	y = []
	if x in main_genres:
		print(x)

for x in itunes_sub:
	if x not in itunes_main:
		print(x)