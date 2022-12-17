modal_keseluruhan = 0
laba_kaseluruhan = 0

#menghitung modal 
modal = harga_barang * barang_terjual

#menghitung modal keseluruhan
modal_keseluruhan = modal_keseluruhan + modal

#menghitung laba
laba = barang_terjual * hargapersen

#menghitung laba keseluruhan
laba_kaseluruhan = laba_kaseluruhan * laba

while (True):

    print("=".center(30,"="))
    nama_barang = input("\nmasukan nama barang     : ")
    harga_barang = int(input("masukan harga barang    : Rp. "))
    barang_terjual = int(input("jumlah barang           : "))
    
    persen = 10 
    hargapersen = int(harga_barang * persen / 100)
    harga_jual = harga_barang + hargapersen

    print("=".center(30,"="))

    print('nama barang             :', nama_barang)
    print('harga barang            : Rp.', harga_barang)
    print('terjual                 :', barang_terjual,)
    print('dijual dengan harga     : Rp.', harga_jual)
    print('keuntuntan per barang   : Rp.', hargapersen)
    print("=".center(30,"="))
    print('modal                   : Rp.', modal_keseluruhan)
    print('laba                    : Rp.', laba)

    apakahlanjut = input("apakah ingin membeli barang lain? Y or N : ")
    if (apakahlanjut != 'Y') :
        break