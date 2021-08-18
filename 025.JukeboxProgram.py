#importing data from antoher python program
from JukeBoxData import albums

while True:
    print("Available Albums:")
    print("================================")
    for index, album in enumerate(albums):
        print("{}: {}".format(index + 1, album[0]))
    print("================================")
    album_choice = int(input("Please Choose Your Album: ")) - 1
    if (album_choice > (len(albums) - 1) or album_choice < 0):
        print("Wrong Choice")
        print()
        continue

    print("Available Songs")
    print("================================")
    for songs in albums[album_choice][3]:
        print("{}: {}".format(songs[0], songs[1]))
    print("================================")
    song_choice = int(input("Please Choose Your Song: ")) - 1
    if (song_choice > (len(albums[album_choice][3]) - 1) or song_choice < 0):
        print("Wrong Choice")
        print()
        continue

    print("Now Playing {}".format(albums[album_choice][3][song_choice][1]))
    print()
