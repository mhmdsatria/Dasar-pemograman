modal_keseluruhan = 0
laba_kaseluruhan = 0

while (True):

    print("=======================================")
    nama_barang = input("\nmasukan nama barang     : ")
    harga_barang = int(input("masukan harga barang    : "))
    barang_terjual = int(input("jumlah barang           : "))
    
    persen = 10
    hargapersen = int(harga_barang * persen / 100)
    harga_jual = harga_barang + hargapersen

    #menghitung modal 
    modal = harga_barang * barang_terjual

    #menghitung modal keseluruhan
    modal_keseluruhan = modal_keseluruhan + modal

    #menghitung laba
    laba = barang_terjual * hargapersen

    #menghitung laba keseluruhan
    laba_kaseluruhan = laba_kaseluruhan * laba

    print("=======================================")

    print('nama barang             :', nama_barang)
    print('harga barang            :', harga_barang)
    print('terjual                 :', barang_terjual,)
    print('dijual dengan harga     :', harga_jual)
    print('keuntuntan per barang   :', harga_barang + hargapersen)
    print("=======================================")
    print('modal                   :', modal_keseluruhan)
    print('laba                    :', laba)

    apakahlanjut = input("apakah ingin membeli barang lain? Y or N : ")
    if (apakahlanjut != 'Y') :
        break