while (True):

    nama_barang = input("\nmasukan nama barang pertama :")
    harga_barang = int(input("masukan harga barang : "))
    barang_terjual = int(input("jumlah barang :"))

    persen = 10
    hargapersen = int(harga_barang * persen / 100)

    print("\n================================")
    print("======== S T R U K B E L I =======")
    print("==================================")
    print("\nmodal                             : Rp.", harga_barang)
    print("harga penjualan per satu barang   : Rp.", harga_barang + hargapersen)
    print("jumlah barang yang terjual        :", barang_terjual, "pcs")
    print("total harga jual                  : Rp.",
        harga_barang * barang_terjual)
    print("keuntungan atau laba              : Rp.",
        barang_terjual * hargapersen)
    print("\n--------------------------------")

    apakahlanjut = input("apakah ingin membeli barang lain? Y or N : ")
    if (apakahlanjut != 'Y') :
        break