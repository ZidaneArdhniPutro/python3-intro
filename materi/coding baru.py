print ("materi 6 - pyhton Data structure")
print ("-----------------------")

# LIST [] (berurutan, bisa diubah, boleh duplikat)
daftar_belanja = [
    "teh desa",# index 0
    "naspad kawan lamo",# index 1
    "pisang kembung",# index 2
    ]

#mengakses list lewat index
print("item ke-4:", daftar_belanja [3])
#remove () mengapus item dari list
daftar_belanja.remove("pisang kembung")
print("isi belanja akhir:", daftar_belanja)

print("------tuple------]")
# tuple (berurut, tidak bisa diubah, boleh duplikat)
#penulisannya menggunaka ()
tgl_lahir = (5, "maret", 1936)
print("tgl lahir urang", tgl_lahir)
# [no index] akses data tuple
print("tanggal:", tgl_lahir[0])
print("bulan:", tgl_lahir[1])
print('tahun:', tgl_lahir[2])


list_minuman = [
    ["jahe", "kencur", "bayem"], #baris 0
    ["terong", ]
]