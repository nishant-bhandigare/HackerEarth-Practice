favourite_singers = {}

n = int(input())
playlist = input()
playlist = playlist.split(" ")

for song in playlist:
    song = int(song)
    if song not in favourite_singers:
        favourite_singers[song] = 1
    else:
        favourite_singers[song] += 1

favourite_singers_list = list(favourite_singers.values())

count = 0
max = 0
for item in favourite_singers_list:
    if item > max:
        max = item

for item in favourite_singers_list:
    if item ==  max:
        count += 1

print(count)