import lyricsgenius as lg
import json
import requests
import random
import re

genius = lg.Genius('mHSelymsgMl5tiiDz8AOKkW0c-ji_26vcWE-uq8sjzm287nhDSmRp3Fh5Ct7N6Uq')
artist = ['Taylor Swift']

# album = genius.search_album("Folklore", "Taylor Swift")
# album.save_lyrics()

with open('Lyrics_Lover.json') as f:
    lyrics_data = json.load(f)

def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values

track_titles = json_extract(lyrics_data, "title")
track_lyrics = json_extract(lyrics_data, "lyrics")

random_song = random.choice(track_titles)
# print(random_song)

random_lyrics = random.choice(track_lyrics)

with open('randomLyrics.txt', 'w') as f:
    f.write(random_lyrics)

"""
with open("randomLyrics.txt", "w") as f:
    for line in lines:
        line = line.replace('[Chorus]','').replace('[Pre-Chorus]','').replace('[Pre-Chorus 2]','').replace('[Bridge]','').replace('[Verse 2]','').replace('[Outro]','').replace('[Post-Chorus]','').rstrip()
        f.write(line)
"""

# Using readlines()
lyrics_file = open('randomLyrics.txt', 'r')
lyrics_lines = lyrics_file.readlines()
# print(lyrics_lines)

first_line = lyrics_lines[0]
sep = ' Lyrics'
song_title = first_line.split(sep, 1)[0]
if song_title == "It’s Nice to Have a Friend":
    song_title == "It's Nice to Have a Friend"
# print(len(song_title))
# print(song_title)

newList = []
for line in lyrics_lines:
    if "Embed" in line: 
        line = re.sub('[0-9]', '', line)
        line = line.replace('Related Songs', '').replace('Embed', '').strip()
    else:
        line = line.strip()
    line = line.replace("\u2005", " ")
    if '"' in line:
        line = line.replace("'", "'") 
    # line = line.replace('Embed', '').strip()
    # line = line.replace('[Verse 1]','\n').replace('[Chorus]','\n').replace('[Pre-Chorus]','\n').replace('[Pre-Chorus 2]','\n').replace('[Bridge]','\n').replace('[Verse 2]','\n').replace('[Outro]','\n').replace('[Post-Chorus]','\n').replace('Embed','\n').rstrip()
    newList.append(line)

newList.pop(0)
# print(newList)

removeList = ['[Intro]', '[Verse 1]', '[Chorus]', '[Pre-Chorus]', '[Pre-Chorus 2]', '[Bridge]', '[Bridge 2]', '[Outro]', '[Verse 2]', '[Post-Chorus]', '[Instrumental bridge]', '[Verse 3]',
              '(Ayy)', 'Uh huh', 'Ah', '(Yeah, yeah, yeah, yeah)', '[Intro: Idris Elba & James Corden]', 'Oh whoa, ah', 'Ooh-ah', '[Verse 2: Taylor Swift]', '[Verse 1: Taylor Swift]', '\n',
              '[Pre-Chorus: Taylor Swift]', '[Chorus: Taylor Swift & The Chicks]', '[Pre-Chorus 1]', '[Intro: Taylor Swift]', '[Chorus: Taylor Swift]', '[Verse 2: Brendon Urie & Taylor Swift]',
              '[Pre-Chorus: Taylor Swift & Brendon Urie, Brendon Urie]', '[Chorus: Brendon Urie, Taylor Swift & Brendon Urie]', '[Bridge: Brendon Urie, Taylor Swift & Both]',
              '[Chorus: Both, Taylor Swift & Brendon Urie]', '[Outro: Brendon Urie, Taylor Swift & Both]', 'Ooh', '[Spoken Outro]', 'Related Songs[Bridge]', "Oh, I'd..."
             ]

afterList = list(set(newList).difference(removeList))
afterList = [i for i in afterList if i]
random_lyric_lines = random.sample(afterList, 3)
print(random_lyric_lines)
first_lyric = random_lyric_lines[0]
second_lyric = random_lyric_lines[1]
third_lyric = random_lyric_lines[2]
print(first_lyric) 
# print(afterList)
# print(random_lyric_line)

# print("Lyrics: " + random_lyric_line)
print("Lyrics: " + first_lyric)
"""
user_guess = input("Guess the song: ").title()
if 'Me' in user_guess:
    user_guess = 'ME!'
if 'Death By A Thousand Cuts' in user_guess:
    user_guess = 'Death by a Thousand Cuts'
# print(user_guess)
if user_guess == song_title:
    correct = True
    print("Correct! YOU ARE A SWIFTIE!")
else:
    print("Wrong. Taylor is disappointed.\nSong is: " + song_title)
"""

incorrect = True 
counter = 0
# while incorrect:
while counter < 5:
    user_guess = input("Guess the song: ").title()
    if 'Me' in user_guess:
        user_guess = 'ME!'
    if 'Death By A Thousand Cuts' in user_guess:
        user_guess = 'Death by a Thousand Cuts'
    if 'Miss Americana And The Heartbreak Prince' in user_guess:
        user_guess = 'Miss Americana & The Heartbreak Prince'
    if (user_guess == "It's Nice To Have A Friend") | (user_guess == "Its Nice To Have A Friend"):
        user_guess = "It’s Nice to Have a Friend"
    if (user_guess == "Soon You'll Get Better") | (user_guess == "Soon Youll Get Better"):
        user_guess = "Soon You’ll Get Better"
    if user_guess == song_title:
        counter += 1
        print("Correct! YOU ARE A SWIFTIE!")
        print("Only took " + str(counter) + " tries.")
        incorrect = True
        break
    else:
        print("Wrong. Taylor is disappointed.")
        counter += 1
        if counter <= 2:
            user_yn = input("Need a hint? (y/n) ").capitalize()
            if user_yn == 'Y' and counter == 1:
                print("Perhaps these lyrics will help: " + second_lyric)
            elif user_yn == 'Y' and counter == 2:
                print("Last hint: " + third_lyric)
            else:
                continue
        else:
            continue
if counter >= 5:
    print("Song is: " + song_title + ". Better luck next time!")











""""

for line in newList:
    if line not in removeList: 
        random_line = random.choice(newList)

# print(random_line)

# Strips the newline character
for line in lyrics_lines:
    line = line.replace('[Chorus]','\n').replace('[Pre-Chorus]','\n').replace('[Pre-Chorus 2]','\n').replace('[Bridge]','\n').replace('[Verse 2]','\n').replace('[Outro]','\n').replace('[Post-Chorus]','\n').replace('Embed','\n').rstrip()
    print(line)
    # print("Lyrics:{}: {}".format(count, line.strip()))

sample_list = random.choice(random.choice(track_lyrics))
# print(sample_list)
song_dict = {track_titles[i]: track_lyrics[i] for i in range(len(track_titles))}
"""


