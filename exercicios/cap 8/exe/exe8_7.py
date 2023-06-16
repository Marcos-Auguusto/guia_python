def make_album(artist, album_title, tracks=None):
    album = {"artist": artist, "album_t": album_title, "tracks": tracks,}
    full_data_album = "Album: " + album["album_t"].title() \
                    + " | Artist: " + album["artist"].title()    
    
    if tracks is not None:
        full_data_album += " | Tracks: " + str(tracks)
    
    return full_data_album

print(make_album("matue", "maquina do tempo", 7))
print(make_album("matue", "conexoes de mafia", 1))
print(make_album("matue", "morte do autotune"))
