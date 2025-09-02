




# Program Profil Digital

# 1. Mengambil data dari pengguna
nama = input(" Masukkan nama lengkap: ")
umur = input(" Masukkan umur: ")
kelas = input(" Masukkan kelas: ")
cita_cita = input(" Masukkan cita-cita atau profesi impian: ")
hobi = input(" Masukkan hobi favorit: ")
belajar = input(" Lebih suka belajar pagi atau malam? ")

# 2. Menampilkan pilihan gaya digital
print("Pilih tipe gaya digital kamu (ketik angkanya saja):")
print("1. Wibu (Anak anime)")
print("2. Gamers")
print("3. Konten Kreator")
print("4. Santai & Chill")
print("5. Produktif")

gaya = input("Pilihan kamu: ")

# 3. Menentukan deskripsi gaya digital berdasarkan pilihan
if gaya == "1":
    deskripsi = "Kamu tipe Wibu sejati! Dunia anime adalah rumah kedua kamu."
elif gaya == "2":
    deskripsi = "Kamu seorang Gamers yang selalu siap push rank!"
elif gaya == "3":
    deskripsi = "Kamu Konten Kreator kreatif, penuh ide dan semangat!"
elif gaya == "4":
    deskripsi = "Kamu santai & chill, hidup tanpa terburu-buru."
elif gaya == "5":
    deskripsi = "Kamu produktif, selalu memanfaatkan waktu sebaik mungkin."
else:
    deskripsi = "Gaya digital kamu unik dan berbeda dari yang lain!"

# 4. Menampilkan hasil profil digital
print(" PROFIL DIGITAL KAMU ")
print(f"Nama       : {nama}")
print(f"Umur       : {umur} tahun")
print(f"Kelas      : {kelas}")
print(f"Cita-cita  : {cita_cita}")
print(f"Hobi       : {hobi}")
print(f"Waktu Belajar Favorit : {belajar}")
print(f"Tipe Gaya Digital : {deskripsi}")