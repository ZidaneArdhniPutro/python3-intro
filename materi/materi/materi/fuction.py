print ("materi 8")
print ('=============')
#fuction di awali dengan keyword 'def'
def halo_dek():
    print("halo dek") 
    print("iya bg")
    print("==========")
#function dengan para meter 'nama'
def halo_ngab(nama):
    print("halo cil", nama)
    print("iya apa bang", nama)
    print("ga papa cil dah sono lanjut", nama)
print("cobain fungsinya:")
halo_dek()
halo_ngab("joko")
halo_ngab("syahid")
halo_ngab("joko")
#fungsi luas persegi panjang
def luas_persegi_panjang(panjang,lebar):
    print("> panjang:", panjang)
    print(">lebar", lebar)
    rumus = panjang * lebar
    print("luas persegi panjang =", rumus)
luas_persegi_panjang(10,20)
luas_persegi_panjang(30,50)
#gas
def kelilingbelahkepan(sisi):
    print("> sisi:", sisi)
    rumus = 4 * sisi
    print ("===========")
    print("keliling belah kepat =", rumus)
kelilingbelahkepan(10)
kelilingbelahkepan(30) 

#function tidak akan di eksekusi
def say_heello(nama):
    print(f"halo mr. {nama}")
    print("baek baek aeee")

say_hello_mini = lambda name: print(f"hallo mr. {name}")   
#panggil function2nya di bawah ini
say_heello("azril")
say_heello("rizki")
print("========")
say_hello_mini("mulyono")
say_hello_mini("sarwono")

#simpel
def sapanama ():
    return "asslamu'alaikum"
print (sapanama())

#funtion dengan parameter 
def sapanama(nama,umur):
    return print(f"asslamu'alaikum{nama},umur kamu{umur}")
sapanama ("-ucok", 13)




