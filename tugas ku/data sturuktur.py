# Tantangan 1: jadwal piket hari ini
jadwalpiket = ['umair', 'zidan', 'azka']
print("jadwal piket hari ini")
for nama in jadwalpiket:
    print(nama)

print()
# 2 rukun iman dan rukun islam

rukun_islam = ['syhadatan', 'sholat', 'zakat', 'puasa', 'haji']
print("rukun islam ada 5")
for i, rukun in enumerate(rukun_islam, start=1):
    print(f"-{i}. {rukun}")
print("=======================================")
# sama yang diatas tapi beda 
rukun_islam = ['syhadatan', 'sholat', 'zakat', 'puasa', 'haji']
print("rukun islam")
for i in range(len(rukun_islam)):
    print(f"{i+1}-> {rukun_islam[i]}") 
print("==================")    
#Tantangan 3: kitab pelajaran  
kitab_pelajaran = 'tauhid', 'fiqih', 'b.arab', 'nahwu'
print("pelajaran di pondok:")
for i, kitab in enumerate (kitab_pelajaran, start=1):
    print(f"{i}. {kitab}")
 #tantangan 4: Bio Date
print('=========================') 
print('Bio data :')
Bio_data = {
    'nama': 'ardhan',
    'umur': 16,
    'kelas': 10,
    'hafalan':10,
}
for key, values in Bio_data.items():
    print(f"{key}, -> {values}") 

