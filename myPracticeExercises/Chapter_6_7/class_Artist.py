# Artist Class

class Artist:
    def __init__(self, artist_name: str):
        self.artist_name = artist_name
        self.albums = []

class Album:
    def __init__(self, album_name: str, artist):
        self.album_name = album_name
        self.artist = artist
        self.tracks = []

class Track:
    def __init__(self, track_number: int, track_name: str, track_length: int):
        self.track_number = track_number
        self.track_name = track_name
        self.track_length = track_length

    def __str__(self):
        return 
        f'''
        \n\t\t\t\t\t{self.artist_name}:
        \nAlbum: {self.album_name}
        \nTracks: {self.tracks}
        '''

artists = []
artist.append(Artist('Mike Parker'))

Envenomations = Album('Envenomations', artists[0])

Resonator_1 = Track(1, 'Resonator_1', 9)