# Nama : Willy Wilsen
# NIM : 16520145
# Tanggal : 1 November 2020
# Deskripsi : Membuat program yang menuliskan bilangan 10^x terkecil yang lebih dari N

# KAMUS
# N : int (Asumsikan N bilangan bulat tak negatif)
# i : int

# ALGORITMA
N = int(input("Masukkan N: "))
if N > 0: # untuk N > 0
    for x in range(999): # looping nilai x
        i = 10**x
        if i <= N: # saat i < N dan i = N, semua i dikali 10
            i = i * 10 # maka akan terdapat satu i yang lebih besar dari N
            if i > N:
                print(i)
elif N == 0: # untuk N = 0
    i = 1
    print(i)
