print("MATERI 7 - PYTHON DATA STRUCTURE")
print("_______________")
#set -> {} -> tidak berurutan, berubah, tidak duplikat

game_azka = {"valoran", "gta", "roblox"}
game_zaky = {"pubg", "delta", "free fire"}
game_azka.add("assasin cread")
game_zaky.add('anggry bert')
game_zaky.remove('free fire')

print("game_azka: ", game_azka )
print("game zaki:", game_zaky)
game_gabungan = game_zaky | game_azka
print("daftar game:", game_gabungan)

# for (loop) untuk mengeluarkan isi item dari set
for game in game_gabungan:
    print('->', game)
    print('--> Transfer data game', game )


kamus_anime = {
    "one_pice": "big mom",
    "scool_dxd": "rias",
    "demon_slayer": "tanjiro",
    "waifu": {
        "one_pice": "hancock",
        "demon_slayer": "nezuko",
    }
}

print("kamus anime:", kamus_anime)
print("mc one pice:",kamus_anime ["one_pice"])
print("mc scool dxd:",kamus_anime ["scool_dxd"])
print('waifu demon slayer:',kamus_anime ["waifu"]["demon_slayer"])

#nambah item baru ke dictionary
kamus_anime ["naruto"] = "hanabi"
print("waifu naruto", kamus_anime, ["naruto"])
#mengubah item dari dictonary
kamus_anime ["demon_slayer"] = "zenitsu"
#mengapus item dari dictonary
del (kamus_anime)['scool_dxd']
print("kamus anime terbaru:", kamus_anime)