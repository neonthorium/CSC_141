def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title()
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who is the artist? "

print("Enter 'q' at any time to quit.")

while True:
    title = input(title_prompt)
    if title == 'q':
        break

    artist = input(artist_prompt)
    if artist == 'q':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")