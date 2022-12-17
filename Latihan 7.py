#Program sesi ke-7
print("==============================================================")
print("============== | Program Matematika Sederhana | ==============")
print("==============================================================")
#mulai proses pemograman

while True :
    print("pilih apa yan akan anda hitung terlebih dahulu?")
    print("[1]luas segitiga")
    print("[2]luas persegi panjang")
    print("[3]menentukan angka genap atau ganjil")
    jawab = input("pilih sesuai nomor di atas :")
    if jawab == "1":
        print("Menghitung Luas Segitiga") #menghitung luas segitiga
        print("Rumus luas Segitiga  1/2 Alas x Tinggi") #rumus
        a1 = int(input("Masukan Alas  : "))
        t2 = int(input("Masukan Tinggi: "))
        luas1 = 1/2 * a1 * t2 #rumus
        print("Luas Segitiga =",(int(luas1))) #hasil luas segitiga
        print("apakah mau melanjutkan? y or n")
        lanjut1 = input()
        if lanjut1 == "y":
            continue 
        else:
            print("Terima kasih")
            break
    elif jawab == "2":
        print("Menghitung Luas Persegi Panjang") #menghitung luas persegi panjang
        print("Rumus Luas Persegi Panjang = Panjang x Lebar") #rumus
        p1 = int(input("Masukan Panjang : "))
        l2 = int(input("Masukan Lebar   : "))
        luas2 = p1*l2 #rumus
        print("Luas Persegi Panjang =",luas2) #hasil luas persegi panjang
        print("apakah mau melanjutkan? y or n")
        lanjut1 = input()
        if lanjut1 == "y":
            continue 
        else:
            print("Terima kasih")
            break
    elif jawab == "3":
        print("berapa angka yang akan anda tentukan?")
        lanjut2 = int(input())
        if lanjut2 % 2 == 0:
            print(" %d Merupakan Bilangan Genap" % lanjut2)
        else:
            print("%d Merupakan Bilangan Ganjil" % lanjut2)
        print("apakah mau melanjutkan? y or n")
        lanjut1 = input()
        if lanjut1 == "y":
            continue 
        else:
            print("Terima kasih")
            break
    else:
        print("yang anda input salah")
    