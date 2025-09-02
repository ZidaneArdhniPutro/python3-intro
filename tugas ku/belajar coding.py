
# Langkah 1: Ambil data dasar dari pengguna
print("Halo! Yuk isi data diri kamu...")

nama = input("Nama lengkap: ")
umur = input("Umur: ")
kelas = input("Kelas: ")
cita_cita = input("Cita-cita atau profesi impian: ")
hobi = input("Hobi favorit: ")
waktu_belajar = input("Lebih suka belajar pagi atau malam? ")

# Langkah 2: Pilih gaya digital
print("1. Wibu (Anak anime banget)")
print("2. Gamer (Ranked jalan terus)")
print("3. K-Popers (Ngikutin gaya Korea)")
print("4. Anak konten (Tiktoker/Youtuber wannabe)")
print("5. Anak nongki (Yang penting ngumpul)")
gaya = input("Pilihan kamu: ")

# Langkah 3: Pertanyaan tambahan sesuai pilihan
tambahan = ""
if gaya == "1":
    tambahan = input("Siapa waifu atau husbando kamu?: ")
    komentar = "bau bawang"
elif gaya == "2":
    tambahan = input("Game favorit kamu apa?: ")
    komentar = "seru tuh" 
elif gaya == "3":
    tambahan = input("Siapa bias kamu?: ")
    komentar = "jeleknyaa"
elif gaya == "4":
    tambahan = input("Platform favorit kamu? TikTok? YouTube?: ")
    print("oo sama dong")
elif gaya == "5":
    tambahan = input("Nongkrong paling sering di mana?: ")
    komentar = "sama gw juga disitu"
else:
    print("Pilihan nggak valid, kita skip bagian ini ya...")

# Langkah 4: Pertanyaan bonus
bonus = input("Apakah teman di sebelah kamu bau? (ya/tidak): ")

# Hasil akhir (bisa dibuat lucu/lengkap)
print("Ini dia data kamu, silakan dicek:")
print("Nama lengkap: ", nama)
print("Umur:  tahun",umur)
print("Kelas: ",kelas)
print("Cita-cita: ",cita_cita)
print("Hobi favorit: ",hobi)
print("Lebih suka belajar: ",waktu_belajar)

gaya_dict = {
    "1": "Wibu (Anak anime banget)",
    "2": "Gamer (Ranked jalan terus)",
    "3": "K-Popers (Ngikutin gaya Korea)",
    "4": "Anak konten (Tiktoker/Youtuber wannabe)",
    "5": "Anak nongki (Yang penting ngumpul)"
}

if gaya in gaya_dict:
    print(f"Tipe gaya digital: {gaya_dict[gaya]}")
    print("Jawaban tambahan:", tambahan)

# Bonus
if bonus.lower == "ya":
    print("Waduh! Kasih tau dia buat mandi ya")
elif bonus.lower == "tidak":
    print("Syukurlah, masih aman guys~")
else:
    print("Gagal ngerti jawaban kamu buat pertanyaan bau itu...")

print("Terima kasih udah isi data! ")

