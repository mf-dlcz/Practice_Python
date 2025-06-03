'''
                Creating a music catalog:
'''

class Artist:
    def __init__(self, name):
        self.name = name
        self.album = []

class Album:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        self.tracks = []

class Track:
    def __init__(self, number, name, length):
        self.number = number
        self.name = name
        self.length = length
        self.artist = []



#*                                       Testing:

# Instatiating Artist objects
art1 = Artist('art1')
art2 = Artist('art2')


# Instiating Album objects
album_1 = Album('album_1', art1)
album_2 = Album('album_2', art2)


# Add albums to the list of albums
art1.album.append(album_1)
art2.album.append(album_2)
