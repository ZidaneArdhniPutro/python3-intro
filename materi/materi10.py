import csv
print('=========file=======')
print("--------------------")

#buka file
file_pesan = open(r"C:\vs code pyhton\materi\materi\pesan.txt","r")
#bacac isi file
isi_pesan = file_pesan.read()
#tampilkan output isi pesan
print(f"ISI PESAN ==>{isi_pesan}")
#tutup file
file_pesan.close()

print("===========open CSV file==========")
file_path_csv = r"C:\vs code pyhton\materi\materi\jajan.csv";
file_jajan = open(file_path_csv,"r")
isi_table_jajan = file_jajan.read()
print(f"TABLE JAJAN ==>{isi_table_jajan}")
file_jajan.close()

print("===append csv file===")
jajan_baru = [6,"syahid",100000]
print(f"jajan baru:{jajan_baru}")
#open() -> pembuka file dari file path
#mode 'a' -> append(tambah data)
#new line -> tambah baris baru dengan teks kosong
# #with... as -> buka file dengan tutup otomatis
with open(file_path_csv, "a",newline="") as file_jajan:
    writer = csv.writer(file_jajan)
    writer.writerow(jajan_baru)

print("-------update csv------")
#baca semua file -> ekstrak data -> buat data baru
#-> tulis ulang semua isi barisnya dgn mode 'w'
#siapkan data jajan kosong untuk menampung data dari csv ke list
data_jajan = []
with open(file_path_csv,"r") as file_jajan:
    #csv reader() -> membaca isi file csv
    isi_table_jajan = csv.reader(file_jajan)
    #ekstrak semua data dgn for loop
    for item_jajan in isi_table_jajan:
        print(item_jajan)
        #taambah kan item ke list data jajan
        data_jajan.append(item_jajan)

#2 . mengubah atau membuat data baru 
for item in data_jajan:
    print(f"proses item no => {item[0]}")
    print(item)  
    #jika kolom nama (index 1 ) adalah 'nama'
    if item[1] == "abdul":
        #ganti kolom uang (index 2) dengan nilai baru 
        uangjajanbaru = 15000
        item[2] = uangjajanbaru     
        print(f"data ditemukan, ganti uang jajan {uangjajanbaru}")
        print('====loop and====')

print(f"DATA JAJAN TERKINI: {data_jajan}") 

#4 tulis ulang deangan mode 'w'
with open (file_path_csv, "w", newline="") as file_jajan:
    writer = csv.writer(file_jajan)
    #.writerwors() -> tulis sekali banyak
    writer.writerows(data_jajan)