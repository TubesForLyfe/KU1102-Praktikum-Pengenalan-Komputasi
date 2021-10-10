# Nama : Willy Wilsen
# NIM : 16520145
# Tanggal : 2 Desember 2020
# Deskripsi : Membuat program  yang  menerima banyaknya kota yang akan dikunjungi Tuan Vin, diikuti posisi masing-masing kota

# KAMUS
# A : int(Asumsikan > 0)
# Jarak(A) : fungsi
# jarak : float
# i : int
# x : int
# y : int
# xt : int
# yt : int
# a : int
# b : int

# ALGORITMA
A = int(input("Masukkan jumlah kota: ")) # input A

def Jarak(A): # membuat fungsi
    jarak = 0 # inisiasi jarak awal

    for i in range(A): # looping koordinat kota
        xt = int(input("Masukkan x kota ke " + str(i+1) + ": "))
        yt = int(input("Masukkan y kota ke " + str(i+1) + ": "))
        if i > 0 : # saat kota > 1
            # jarak kota baru dengan kota sebelumnya
            x = abs(xt-a)
            y = abs(yt-b)
            jarak += (x**2 + y**2)**0.5 # pythagoras
        # koordinat kota sebelumnya
        a = xt
        b = yt
    return jarak # mengembalikan jarak
    
print("Jarak totalnya", Jarak(A)) # print
