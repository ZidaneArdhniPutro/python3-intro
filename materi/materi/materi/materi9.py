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
#sorted() -> mengurutkan data 
jajanmingguan= [50000, 30000, 70000, 45000]
urutkanuang= sorted(jajanmingguan)
urutkanuangterbalik= sorted(jajanmingguan, reverse=True)
print(f"urutan uang:{urutkanuang}")
print(f"urutan uang terbalik: {urutkanuangterbalik}")
#map() -> mentransformasi data
nambahinuang= map(lambda uang :uang+5000, jajanmingguan)
#list() mengubah data objek map menjadi benk list
nambahinduit = list(nambahinuang)
print(f"map uang berkurang: {nambahinduit}")
print("=========")
