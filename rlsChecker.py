import time
import winsound
import tkinter.simpledialog as tksd
import feedparser
import re
import os
from pushover import Client


client = Client("u4a9fk7gyxgz8yb8xngvj9fyuuj673", api_token="a42t226ott7n15yi3brhvoop8bzjad")

startTime = time.clock()

feed = feedparser.parse('http://predb.me/?cats=games-pc&rss=1')

found_list = []

def game_found(result):
    if result in found_list:
        print("Already found: " + result)
        return
    else:
        print(result + " exists on predb.me")
        client.send_message(result + " exists on PreDB.me", title="Game release")
        winsound.Beep(200, 1000)
        found_list.append(result)


def main_loop(release):
    count = 0
    while count < 20:
        result = feed['entries'][count].title.split("/n")
        count = count + 1

        for game in result:
            if re.search(release, game, re.IGNORECASE):
                game_found(game)


def getUptime():
    timeSeconds = time.clock() - startTime
    timeMinutes = timeSeconds / 60
    humanTime = str(round(timeMinutes, 0))
    print("Time Elapsed: " + humanTime + " Minutes")
    return

# GUI Drawing + Focus settings
root = tksd.Tk()
root.withdraw()
root.lift()
root.focus_force()

release = tksd.askstring("Release", "search for release:")
while True:
    os.system("cls")
    print("Searching for " + release.upper())
    getUptime()
    main_loop(release)
    time.sleep(60)

