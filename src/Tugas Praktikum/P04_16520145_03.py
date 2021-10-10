# Nama : Willy Wilsen
# NIM : 16520145
# Tanggal : 2 Desember 2020
# Deskripsi : Membuat program  yang  menerima banyaknya baris dan kolom matriks, kemudian membuat fungsi yang mengeluarkan matriks seperti pada soal

# KAMUS
# M : int
# N : int
# peubah(M,N) : fungsi
# Matriks : matriks
# i : int
# j : int
# k : int

# ALGORITMA
M = int(input("Masukkan baris: "))
N = int(input("Masukkan kolom: "))

def peubah(M,N):
    T = [[0 for j in range(N)] for i in range(M)]
    if (M == N):
        for i in range(M):
            T[i][i] = 1
    elif (M == (N+1)):
        for i in range(N//2+1):
            T[i][i] = 1
            T[M-i-1][N-i-1] = 1
    elif (M > (N+1)):
        i = 1
        while (i < (M-N)):
            j = i
            k = 0
            while (k < N):
                T[j][k] = 1
                k += 1
                j += 1
            i += 1
        for i in range(N//2+1):
            T[i][i] = 1
            T[M-i-1][N-i-1] = 1
    elif (N == (M+1)):
        for i in range(M//2+1):
            T[i][i] = 1
            T[M-i-1][N-i-1] = 1
    elif (N > (M+1)):
        i = 1
        while (i < (N-M)):
            j = i
            k = 0
            while (k < M):
                T[k][j] = 1
                k += 1
                j += 1
            i += 1
        for i in range(M//2+1):
            T[i][i] = 1
            T[M-i-1][N-i-1] = 1
    return T

Matriks = peubah(M,N)
for i in range(M):
    for j in range(N):
        print(Matriks[i][j], end="")
    print()
