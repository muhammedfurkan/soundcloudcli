#!/usr/bin/python2
# encoding=utf8
# pylint: disable=print-statement
import soundcloud
import os
import sys
import getpass
import string

reload(sys)
sys.setdefaultencoding('utf8')

if not sys.platform.startswith('linux'):
  print("This script can only be run under Linux.")
  sys.exit(0)

tracks = None
stream_url = None
thist = None
client = soundcloud.Client(client_id='LBCcHmRB8XSStWL6wKH2HPACspQlXg2P')

def error_noquery():
  print("No query sent! Please search for a song.")

def error_nosong():
  print("You haven't played any song yet.")

if not os.path.isdir("/home/" + getpass.getuser() + "/Downloads"):
  os.system("mkdir ~/Downloads")

def download():
  try:
    printable = set(string.printable)
    artist = filter(lambda x: x in printable, thist.title.split(" - ")[0])
    printable = set(string.printable)
    title = filter(lambda x: x in printable, thist.title.split(" - ")[1])
    if x == "":
      os.system("wget \"" + stream_url.location + "\" -O .cache.mp3")
      os.system("sacad \"" + artist + "\" \"" + title + "\" 800 .cover.jpg")
      os.system("lame -V0 --ti .cover.jpg --ta \"" + artist + "\" --tt \"" + title + "\" .cache.mp3 \"/home/" + getpass.getuser() + "/Downloads/" + filename + "\"")
      os.system("rm .cover.jpg")
      os.system("rm .cache.mp3")
    else:
      os.system("wget \"" + stream_url.location + "\" -O .cache.mp3")
      os.system("sacad " + artist + " " + title + " 800 .cover.jpg")
      os.system("lame -V0 --ti .cover.jpg --ta \"" + artist + "\" --tt \"" + title + "\" .cache.mp3 \"" + filename + "\"")
      os.system("rm .cover.jpg")
      os.system("rm .cache.mp3")
  except:
    printable = set(string.printable)
    artist = filter(lambda x: x in printable, thist.user['username'])
    printable = set(string.printable)
    title = filter(lambda x: x in printable, thist.title)
    if x == "":
      os.system("wget \"" + stream_url.location + "\" -O .cache.mp3")
      os.system("sacad \"" + artist + "\" \"" + title + "\" 800 .cover.jpg")
      os.system("lame -V0 --ti .cover.jpg --ta \"" + artist + "\" --tt \"" + title + "\" .cache.mp3 \"/home/" + getpass.getuser() + "/Downloads/" + filename + "\"")
      os.system("rm .cover.jpg")
      os.system("rm .cache.mp3")
    else:
      os.system("wget \"" + stream_url.location + "\" -O .cache.mp3")
      os.system("sacad \"" + artist + "\" \"" + title + "\" 800 .cover.jpg")
      os.system("lame -V0 --ti .cover.jpg --ta \"" + artist + "\" --tt \"" + title + "\" .cache.mp3 \"" + filename + "\"")
      os.system("rm .cover.jpg")
      os.system("rm .cache.mp3")

print("soundcli 0.2")
print("(C) 2018 koyu.space Developers")
print

while True:
  sys.stdout.write("soundcli> ")
  sys.stdout.flush()
  try:
    x = raw_input()
  except:
    sys.exit(0)
  counter = 0
  if x.startswith("search "):
    tracks = client.get('/tracks', q=x.split("search ")[1])
    for track in tracks:
      counter = counter + 1
      print(str(counter) + ": " + track.title)
  if x.startswith("play "):
    try:
      thist = None
      for track in tracks:
        counter = counter + 1
        if str(counter) == x.split("play ")[1]:
          thist = track
      stream_url = client.get(thist.stream_url, allow_redirects=False)
      os.system("mpv \"" + stream_url.location + "\"")
    except:
      error_noquery()
  if x == "list" or x == "ls":
    if not tracks == None:
      for track in tracks:
        counter = counter + 1
        print(str(counter) + ": " + track.title)
    else:
      error_noquery()
  if x.startswith("download"):
    if x == "download":
      if not stream_url == None:
        filename = thist.title.replace(" ", "_").replace("!", "_").replace("&", "_").replace("?", "_") + ".mp3"
        sys.stdout.write("Download location (Enter for ~/Downloads): ")
        sys.stdout.flush()
        x = raw_input()
        download()
      else:
        error_nosong()
    else:
      for track in tracks:
        counter = counter + 1
        if str(counter) == x.split("download ")[1]:
          thist = track
      stream_url = client.get(thist.stream_url, allow_redirects=False)
      filename = thist.title.replace(" ", "_").replace("!", "_").replace("&", "_").replace("?", "_") + ".mp3"
      sys.stdout.write("Download location (Enter for ~/Downloads): ")
      sys.stdout.flush()
      x = raw_input()
      download()
  if x == "help":
    print
    print("soundcli help:")
    print("search <query>: searchs a song on soundcloud")
    print("ls/list: lists the songs again")
    print("play <#song>: plays song from list")
    print("download [#song]: Downloads the given song")
    print
