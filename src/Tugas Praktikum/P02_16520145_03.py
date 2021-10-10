# Nama : Willy Wilsen
# NIM : 16520145
# Tanggal : 4 November 2020
# Deskripsi : Membuat program yang menggambarkan pola sebuah kotak 2N*2N

# KAMUS
# N : int
# Asumsikan N > 0

# ALGORITMA
N = int(input("Masukkan bilangan: "))
T = [[0 for j in range(2*N)] for i in range(2*N)]
print("Pola yang terbentuk:")
for i in range(1,N):
    for j in range(i,N):
        T[i][j] = i % 10
        T[i][2*N-j-1] = i % 10
        T[2*N-i-1][j] = i % 10
        T[2*N-i-1][2*N-j-1] = i % 10
        T[j][i] = i % 10
        T[j][2*N-i-1] = i % 10
        T[2*N-j-1][i] = i % 10
        T[2*N-j-1][2*N-i-1] = i % 10

for i in range(2*N):
    for j in range(2*N):
        print(T[i][j], end = "")
    print()
