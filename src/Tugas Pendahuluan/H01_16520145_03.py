# Nama : Willy Wilsen
# NIM : 16520145
# Tanggal : 16 Oktober 2020
# Deskripsi : Membuat program yang mengecek apakah X bilangan positif genap,
# positif ganjil, negatif, atau nol

# KAMUS
# X : integer

# ALGORITMA
X = int(input("Masukkan X: "))

if (X > 0):
    if (X % 2 == 0):
        print("X adalah bilangan positif genap")
    else:
        print("X adalah bilangan positif ganjil")
elif (X == 0):
    print("X adalah bilangan nol")
else:
    print("X adalah bilangan negatif")
