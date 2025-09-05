import json
print('====print====')
print('===read json===')
file_path_json = r"C:\vs code pyhton\materi\materi\materi1.json"
with open (file_path_json, "r") as file_materi:
    #json.load() -> membaca isi file json
    data_materi = json.load(file_materi)
    print(f"judul berkas : {data_materi['title']}")
    print(f"total kelas a : {data_materi['statussantri']}")
    print(f"stasus santri: {data_materi['statussantri']}")
    print(f":pelajaran santri {data_materi['pelajaran']}")

#akses data list dengan for loop
for pelajalaran in data_materi ['pelajaran']:
    print(f"-- {pelajalaran}")

print("-"*50)
print("| no | nama surah | ayat | tempat turun|")
print("-"*50)
for surah in data_materi['surah']:
    print(f"| {surah['no']} | {surah['nama']} |{surah['ayat']} | {surah['turun']} |")












   
    