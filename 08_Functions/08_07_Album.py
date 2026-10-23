def make_album(artist, title, num_songs=0):
    """Build a dictionary containing information about an album."""
    album = {
        'artist': artist.title(),
        'title': title.title()
    }
    if num_songs:
        album['num_songs'] = num_songs
    return album

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('nirvana', 'nevermind')
print(album)

album = make_album('American Football', 'american football')
print(album)

album = make_album('pink floyd', 'the wall', 26)
print(album)