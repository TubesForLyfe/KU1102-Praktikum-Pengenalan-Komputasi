# Nama : Willy Wilsen
# NIM : 16520145
# Tanggal : 1 November 2020
# Deskripsi : Membuat program yang menentukan apakah X adalah bilangan prima

# KAMUS
# X : int (Asumsikan X bilangan asli)
# Prima : boolean

# ALGORITMA
X = int(input("Masukkan X: "))
Prima = True
for i in range(2,X):
    if X % i == 0: # untuk mencari faktor dari X
        Prima = False
    elif X == 1:
        Prima = False

if Prima == False:
    print(X, "bukan bilangan prima")
else:
    print(X, "adalah bilangan prima")
