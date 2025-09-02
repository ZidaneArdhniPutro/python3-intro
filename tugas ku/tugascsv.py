import csv
 
filepath= r"C:\belajar git basic sma it HSI IT purworejo\tugas ku\tugascsv.csv"

with open (filepath,"r") as filebaru:
    next(filebaru)
    read = csv.reader(filebaru)
    listread = list(read)

print("Tanggal | Keterangan | Kategori | Jumlah")
print("-"*30)
for baris in listread:
     tanggal=baris[0]
     keterangan=baris[1]
     katagori =baris[2]
     jumlah= baris[3]

     print (f"{tanggal} | {keterangan} | {katagori} | {jumlah}")

with open (filepath, "a", newline="") as filebaru:
     writh = csv.writer(filebaru)
     writh.writerow(["5", "faiz", "10"]) 