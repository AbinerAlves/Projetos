print("="*45)
print(" EXERCÍCIO - A Playlist do Fudencio")
print("="*45)

playlist = ["zézé de amargo", "Religião urbana", "Narvile", "Franguito lopes", "Raul seitas", "BTS"]

playlist.append("Xitadinho e chororou")
playlist.append("P.Diddy Bieber")

playlist.remove("BTS")

playlist.sort()
print("Sua Playlist final:")
for musica in playlist:
    print(musica)