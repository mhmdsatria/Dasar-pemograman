#deskriptif
#membuat variable nama barang
#membuat variable harga barang
#membuat variable presentasi harga
#input nama barang
#input harga barang 
#harga barang * presentasi
#print harga barang beserta nama barang

namabarang = input("masukan nama barang :")
hargabarang = int (input("masukan harga barang :"))
nama_barang = input("masukan nama barang :")
harga_barang = int (input("masukan harga barang :"))
_namabarang = input("masukan nama barang :")
_hargabarang = int (input("masukan harga barang :"))

a = 10
persen = (a/100)
print("\n")
print("nama barang =",namabarang)
hargajual = int (hargabarang * persen)
print ("keuntungan =",hargajual)
print("harga total=",hargabarang + hargajual)
print("\n")
print("nama barang =",nama_barang)
hargajual = int (harga_barang * persen)
print ("keuntungan =",hargajual)
print("harga total=",harga_barang + hargajual)
print("\n")
print("nama barang =",_namabarang)
hargajual = int (_hargabarang * persen)
print ("keuntungan =",hargajual)
print("harga total=",_hargabarang + hargajual)
