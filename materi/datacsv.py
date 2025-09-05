import csv
 
filepath= r"C:\belajar git basic sma it HSI IT purworejo\materi\materi\materi\data.csv"

with open (filepath,"r") as filebaru:
    next(filebaru)
    read = csv.reader(filebaru)
    listread = list(read)

print("SEMUA DATA")
print("-"*20)
for baris in listread:
     nomor=baris[0]
     nama=baris[1]
     kelas =baris[2]

     print (f"{nomor} | {nama} | {kelas}")

# TAMBAH DATA 
with open (filepath, "a", newline="") as filebaru:
    writh = csv.writer(filebaru)
    writh.writerow(["4", "faiz", "10"])      