# Nama : Willy Wilsen
# NIM : 16520145
# Tanggal : 18 November 2020
# Deskripsi : Membuat program yang mencari panjang dari substring terpanjang yang merupakan palindrom.

# KAMUS
# N : int (Asumsikan lebih dari 0)
# X : str
# cek : str
# panjang : int
# max_palindrom : int
# sum_palindrom : int
# i : int
# j : int

# ALGORITMA
N = int(input("Masukkan panjang string: ")) # input N
X = str(input("Masukkan string: ")) # input X
panjang = 1
max_palindrom = 0

if (len(X) == N): # saat sesuai
    while (panjang <= len(X)):
        i = 0
        while (i <= (len(X)-panjang)):
            palindrom = True
            cek = ""
            j = i
            while (j < (panjang + i)):
                cek += X[j]
                j += 1
            j = 0
            while (j < len(cek) and palindrom):
                if (cek[j] != cek[len(cek)-j-1]):
                   palindrom = False
                j += 1
            if (palindrom):
                sum_palindrom = len(cek)
            if (sum_palindrom > max_palindrom):
                max_palindrom = sum_palindrom
            i += 1
        panjang += 1
    print("Panjang palindrom string adalah", max_palindrom)
else: # saat tidak sesuai
    print("Maaf, panjang string tidak sesuai")
