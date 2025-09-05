# list
pekerjaan = ['nganggur', 'kantoran', 'mulung']
print(pekerjaan[2])
pekerjaan[1] = 'pemadam'
print(pekerjaan)


# 3. menambah element
pekerjaan.append('guru')
print(pekerjaan)

# di index terserah
pekerjaan.insert (0,'masinis')
print(pekerjaan)

# 4 mengapus item
pekerjaan.remove('mulung')
print(pekerjaan)

# mengapus berdasarkan index
pekerjaan.pop(1)
print(pekerjaan)

5#panjang list
print(len(pekerjaan)) 

#6 mencetak seluruh isi list menggunakan looping
for hitam in pekerjaan:
    print(hitam)
