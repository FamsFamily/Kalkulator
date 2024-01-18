def penjumlahan(a, b):
    print("Hasilnya:",a + b)
    
def pengurangan(a, b):
    print("Hasilnya:",a - b)

def perkalian(a,b):
    print ("Hasilnya:",a * b)
    
def pembagian(a,b):
    print ("Hasilnya:",a / b)
    
def pembagian_bilangan_bulat(a,b):
    print ("Hasilnya:",a // b)
    
def perpangkatan(a,b):
    print ("Hasilnya:",a ** b)
    
operasi = ["penjumlahan","pengurangan","perkalian","pembagian","pembagian bilangan bulat","perpangkatan"]

print("KALKULATOR")
while True:
    print("\n",operasi)
    pilih = input("Pilih operasi:")
    if pilih == operasi[0]:
        x = int(input("Masukkan angka pertama:"))
        y = int(input("Masukkan angka kedua:"))
        penjumlahan(x,y)
    elif pilih == operasi[1]:
        x = int(input("Masukkan angka pertama:"))
        y = int(input("Masukkan angka kedua:"))
        pengurangan(x,y)
    elif pilih == operasi[2]:
        x = int(input("Masukkan angka pertama:"))
        y = int(input("Masukkan angka kedua:"))
        perkalian(x,y)
    elif pilih == operasi[3]:
        x = int(input("Masukkan angka pertama:"))
        y = int(input("Masukkan angka kedua:"))
        pembagian(x,y)
    elif pilih == operasi[4]:
        x = int(input("Masukkan angka pertama:"))
        y = int(input("Masukkan angka kedua:"))
        pembagian_bilangan_bulat(x,y)
    elif pilih == operasi[5]:
        x = int(input("Masukkan angka pertama:"))
        y = int(input("Masukkan angka kedua:"))
        perpangkatan(x,y)
