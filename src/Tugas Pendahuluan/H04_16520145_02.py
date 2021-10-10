# Nama : Willy Wilsen
# NIM : 16520145
# Tanggal : 29 November 2020
# Deskripsi : Membuat program matriks A berukuran N×M dan menuliskan berapa banyak bilangan positif matriks beserta isi matriks itu sendiri

# KAMUS
# A : array(matriks)
# N : int(baris matriks)
# M : int(kolom matriks)
# i : int(indeks baris)
# j : int(indeks kolom)
# positif : int

# ALGORITMA
N = int(input("Masukkan N: ")) # input N
M = int(input("Masukkan M: ")) # input M
A = [[0 for j in range(M)] for i in range(N)] # membuat matriks A
positif = 0 # inisiasi positif

for i in range(N):
    for j in range(M):
        A[i][j] = int(input("Masukkan nilai A[" + str(i+1) + "][" + str(j+1) + "]: ")) # input matriks A
        if A[i][j] > 0: # saat indeks positif
            positif += 1

print("Ada", positif, "bilangan positif di matriks") # print banyaknya positif
for i in range(N):
    for j in range(M):
        print(A[i][j], end =" ") # print isi matriks
    print("") # memberi jarak per baris
