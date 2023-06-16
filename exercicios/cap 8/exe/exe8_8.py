album = []

def add_album(artist, album_title, tracks=None):
    register_album = {"artist": artist, "album_title": album_title, \
                      "tracks": tracks,}
    album.append(register_album)
    print("Album registrado com sucesso!")

def view_albums():
    if len(album) > 0:
        for all_albums in album:   
            print(f"Album: {all_albums['album_title']}")
            print(f"Artista: {all_albums['artist']}")
            print(f"Tracks: {all_albums['tracks']}")
    else:
        print("Não tem albums registrados!")

while True:
    
    print("1 - Inserir album")
    print("2 - Mostrar albuns")
    print("3 - Sair")
    option = input("Selecione uma opcao: ")

    if option == "1":
        name_album = input("Nome do album: ")
        name_artist = input("Nome do artista: ")
        number_tracks = input("Números de tracks: ")
        add_album(name_artist, name_album, number_tracks)
    
    elif option == "2":
        data_albums = view_albums()
        print(data_albums)
    elif option == "3":
        break
