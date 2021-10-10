# Nama : Willy Wilsen
# NIM : 16520145
# Tanggal : 4 November 2020
# Deskripsi : Membuat program yang menampilkan kelipatan dari A, B, dan C

# KAMUS
# N : int
# a : int
# b : int
# c : int
# x : int
# Asumsikan N > 0 dan a, b , c  > 0

# ALGORITMA
N = int(input("Masukkan nilai N: ")) # input N
a = int(input("Masukkan nilai a: ")) # input a
b = int(input("Masukkan nilai b: ")) # input b
c = int(input("Masukkan nilai c: ")) # input c

# loop dari 1 sampai N
for x in range(1,N+1):
    if x % a == 0 and x % b != 0 and x % c != 0: # jika x kelipatan a
        k = "Siap"
        print(k, end =" ")
    elif x % b == 0 and x % a != 0 and x % c != 0: # jika x kelipatan b
        k = "Bang"
        print(k, end =" ")
    elif x % c == 0 and x % b != 0 and x % a != 0: # jika x kelipatan c
        k = "Jago"
        print(k, end =" ")
    elif x % a == 0 and x % b == 0 and x % c != 0: # jika x kelipatan a dan kelipatan b
        k = "SiapBang"
        print(k, end =" ")
    elif x % a == 0 and x % c == 0 and x % b != 0: # jika x kelipatan a dan kelipatan c
        k = "SiapJago"
        print(k, end =" ")
    elif x % c == 0 and x % b == 0 and x % a != 0: # jika x kelipatan c dan kelipatan b
        k = "BangJago"
        print(k, end =" ")
    elif x % a == 0 and x % b == 0 and x % c == 0: # jika x kelipatan a, kelipatan b, dan kelipatan c
        k = "SiapBangJago"
        print(k, end =" ")
    else: # jika x bukan kelipatan a, b , dan c
        print(x, end =" ")
