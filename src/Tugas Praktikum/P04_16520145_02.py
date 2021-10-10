# Nama : Willy Wilsen
# NIM : 16520145
# Tanggal : 2 Desember 2020
# Deskripsi : Membuat program mengeluarkan matriks yang berisi angka-angka

# KAMUS
# A : int
# B : int
# T : matriks

# ALGORITMA
A = int(input("Masukkan jumlah baris matriks: ")) # input A
B = int(input("Masukkan jumlah kolom matriks: ")) # input B
T = [["*" for j in range(B)] for i in range(A)] # membuat matriks
a = 0 # inisiasi a

for i in range(A):
    for j in range(B):
        T[i][j] = str(input("Masukkan elemen baris "+str(i+1)+" kolom "+str(j+1)+": ")) # input isi matriks
        
for i in range(A):
    for j in range(B):
        if T[i][j] == "*": # saat matriks berupa *
            T[i][j] = "#"
        elif T[i][j] == ".": # saat tidak *
            # conditional
            if i != 0 and j != 0 and i != A-1 and j != B-1:
                a = 0
                for k in range(i-1,i+2):
                    for l in range(j-1,j+2):
                        if T[k][l] == "*" or T[k][l] == "#":
                            a += 1
            elif i == 0 and j == 0:
                a = 0
                for k in range(i,i+2):
                    for l in range(j,j+2):
                        if T[k][l] == "*" or T[k][l] == "#":
                            a += 1
            elif i == 0 and j == B - 1:
                a = 0
                for k in range(i,i+2):
                    for l in range(j-1,j+1):
                        if T[k][l] == "*" or T[k][l] == "#":
                            a += 1
            elif i == A - 1 and j == B - 1:
                a = 0
                for k in range(i-1,i+1):
                    for l in range(j-1,j+1):
                        if T[k][l] == "*" or T[k][l] == "#":
                            a += 1
            elif i == A - 1 and j == 0:
                a = 0
                for k in range(i-1,i+1):
                    for l in range(j,j+2):
                        if T[k][l] == "*" or T[k][l] == "#":
                            a += 1
            elif i == 0 and j != B - 1 and j != 0:
                a = 0
                for k in range(i,i+2):
                    for l in range(j-1,j+2):
                        if T[k][l] == "*" or T[k][l] == "#":
                            a += 1
            elif i == A - 1 and j != B - 1 and j != 0:
                a = 0
                for k in range(i-1,i+1):
                    for l in range(j-1,j+2):
                        if T[k][l] == "*" or T[k][l] == "#":
                            a += 1
            elif j == 0 and i != A - 1 and i != 0:
                a = 0
                for k in range(i-1,i+2):
                    for l in range(j,j+2):
                        if T[k][l] == "*" or T[k][l] == "#":
                            a += 1
            elif j == B - 1 and i != A - 1 and i != 0:
                a = 0
                for k in range(i-1,i+2):
                    for l in range(j-1,j+1):
                        if T[k][l] == "*" or T[k][l] == "#":
                            a += 1
            T[i][j] = a
            
print("Matriks angka:") 
for i in range(A): # print matriks
    for j in range(B):
        print(T[i][j], end = "")
    print()
