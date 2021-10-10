# Nama : Willy Wilsen
# NIM : 16520145
# Tanggal : 18 November 2020
# Deskripsi : Membuat program deretan angka sebagai indeks dari array dan menerjemahkan deretan angka tersebut dengan huruf yang sesuai dalam array.

# KMAUS
# A : array
# N : int (Asumsikan lebih dari 0)
# X : str (Isi string berupa angka)
# i : int (indeks array X)
# C : int (indeks array A)

# ALGORITMA
A = [" ","A","B","E","I","K","L","R","T","U"]
N = int(input("Masukkan banyaknya bilangan: ")) # input N
X = str(input("Masukkan bilangan: ")) # input X

if len(X) == N: # saat sesuai
    for i in range(N): # dari indeks 0 sampai N-1
        C = int(X[i]) # C adalah  indeks A
        print(A[C], end = "") # print
else: # saat tidak sesuai
    print("Maaf, banyaknya bilangan tidak sesuai")
