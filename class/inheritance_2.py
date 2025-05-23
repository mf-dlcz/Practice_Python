"""
Create a group of classes that represents information about music artists, 
their albums, and the tracks on those albums.  

Each class should contain the following information:
    Artist:  name, released albums
    Album: name, artist, tracks
    Track: number, name, length (seconds)

Demonstrate ways to navigate the relationships between the classes.
List every track from every album published for an artist.
List the album, number of tracks, and the total run time of the album for each artist.
"""

class Artist:
    def __init__(self, name):
        self.name =name
        self.albums = []
        
    def __str__(self):
        return self.name
        
class Album:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.tracks = []
        
    def __str__(self):
        return f'{self.title} by {self.artist}'
        
class Track:
    def __init__(self, number, song_name, length):
        self.number = number
        self.song_name = song_name
        self.length = length
        
    def __str__(self):
        return f'{self.number}: {self.song_name} ({self.length}s)'
    

###################################
# Main thread of execution

# create some objects

artists = []
artists.append(Artist('Zyaeson'))
artists.append(Artist('Froggy'))

# create some albums
album1 = Album('Code Heaven', artists[0])
artists[0].albums.append(album1)
album1.tracks.append(Track(1, 'Binary Solo', 256))
album1.tracks.append(Track(2, 'End of line blues', 128))

album2 = Album('Colorful Days', artists[1])
artists[1].albums.append(album2)
album2.tracks.append(Track(1, 'Blue Frog', 120))
album2.tracks.append(Track(2, 'Happy Pig', 240))
album2.tracks.append(Track(3, 'Banjo Songs', 225))

album3 = Album("Second Opus", artists[0])
artists[0].albums.append(album3)
album3.tracks.append(Track(1, "Towering Oaks", 150))
album3.tracks.append(Track(2, "Lofty Cedars", 138))

# List every track from every album published for an artist.

# artist = artists[0]
for artist in artists:
    print(artist.name)
    for album in artist.albums:
        print(f' Album: {album.title}')
        for track in album.tracks:
            print(f'\t{track}')



# List the album, number of tracks, and the total run time of the album for each artist.
for artist in artists:
    print(artist.name)
    for album in artist.albums:
        runtime = 0
        for track in album.tracks:
            runtime += track.length
        
        print(f' {album.title} : Tracks({len(album.tracks)}) Runtime: {runtime}')