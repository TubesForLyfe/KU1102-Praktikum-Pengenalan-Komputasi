# Nama : Willy Wilsen
# NIM : 16520145
# Tanggal : 4 November 2020
# Deskripsi : Membuat program yang menampilkan FPB dari bilangan-bilangan

# KAMUS
# a : int
# b : int
# c : int
# d : int
# x : int
# Asumsikan tidak ada yang negatif

# ALGORITMA
# input a,b,c,d
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))
d = int(input("Masukkan bilangan keempat: "))

x = min(a,b,c,d) # FPB terbesar
while x >= 1: # urutan dari terbesar hingga terkecil
    if a % x == 0 and b % x == 0 and c % x == 0 and d % x == 0: # untuk mencari FPB 4 bilangan tersebut
        print("FPB dari keempat bilangan tersebut adalah", x)
        x = 0 # setelah ditemukan, program berhenti
    x -= 1 # apabila tidak ditemukan, program akan terus mencari hingga dapat
