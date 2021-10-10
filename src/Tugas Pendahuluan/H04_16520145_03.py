# Nama : Willy Wilsen
# NIM : 16520145
# Tanggal : 29 November 2020
# Deskripsi : Membuat program menerima N dan menuliskan matriks segitiga pascal berukuran N×N

# KAMUS
# N : int(ukuran baris dan kolom matriks)
# A : array(matriks)
# i : int(indeks baris)
# j : int(indeks kolom)

# ALGORITMA
N = int(input("Masukkan N: ")) # input N
A = [[1 for j in range(N)] for i in range(N)] # membuat matriks A

for i in range(1,N): # dari baris 2
    for j in range(1,N): # dari kolom 2
        A[i][j] = A[i-1][j] + A[i][j-1] # membuat segitiga pascal

for i in range(N):
    for j in range(N):
        print(A[i][j], end =" ") # print matriks A
    print("") # memberi jarak per baris
