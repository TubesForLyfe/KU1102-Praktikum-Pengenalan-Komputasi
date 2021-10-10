# Nama : Willy Wilsen
# NIM : 16520145
# Tanggal : 15 November 2020
# Deskripsi : Membuat program yang menerima N bilangan dan menuliskan kembali kebalikan bilangan tersebut

# KAMUS
# N : int
# Tab : array
# i : int(indeks Tab)

# ALGORTIMA
N = int(input("Masukkan N: "))
Tab = [0 for i in range(N)] # mendeklarasi array

for i in range(N): # memasukkan isi pada array
    Tab[i] = int(input())

# menuliskan kembali bilangan secara terbalik
print("Hasil dibalik:")
for i in range(N-1,-1,-1): # indeks array dibalik
    Tab[i] = Tab[i]
    print(Tab[i])
