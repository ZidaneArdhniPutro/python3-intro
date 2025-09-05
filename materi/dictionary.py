print("pengulangan dictionary")
#Dictionary
z_a_p = {
    'umur': 16,
    'asal': 'beksai',
    'kls': '10'
}
#operasi pada Dictionary

#mengakses nilai
print(z_a_p['umur'])

# 2. menambah nilai
z_a_p["berat badan"]= 57
print(z_a_p)

#mengubah nilai
z_a_p["berat badan"]= 87
print(z_a_p)

# Mengapus nilai
del (z_a_p)['berat badan']
print(z_a_p)

# Mengecek key
print("nama" in z_a_p)

# mendapatkan semua key apa aja
print(z_a_p.keys())

#cara ngecek ada value apa saja 
print(z_a_p.values())

# Loop
for key in z_a_p:
    print(z_a_p)

for values in z_a_p.values():
    print(values)  

for key, values in z_a_p.items():
    print(f"{key}, -> {values}")    



