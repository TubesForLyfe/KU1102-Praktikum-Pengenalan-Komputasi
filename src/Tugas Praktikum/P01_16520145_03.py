# Nama : Willy Wilsen
# NIM : 16520145
# Tanggal : 21 Oktober 2020
# Deskripsi : Membuat program mencari jarak terpendek

# KAMUS
# x1 = int
# y1 = int
# x2 = int
# y2 = int
# x3 = int
# y3 = int

# ALGORITMA
x1 = int(input("Masukkan x1: "))
y1 = int(input("Masukkan y1: "))
x2 = int(input("Masukkan x2: "))
y2 = int(input("Masukkan y2: "))
x3 = int(input("Masukkan x3: "))
y3 = int(input("Masukkan y3: "))

# untuk mencari jarak terpendek
if abs(x1) + abs(y1) < abs(x2) + abs(y2):
        print ("Jarak terpendeknya adalah", str(abs(x1) + abs(y1) + abs(x2-x1) + abs(y2-y1) + abs(x2-x3) + abs(y2-y3)))
else:
        print ("Jarak terpendeknya adalah", str(abs(x2) + abs(y2) + abs(x2-x1) + abs(y2-y1) + abs(x1-x3) + abs(y1-y3)))
