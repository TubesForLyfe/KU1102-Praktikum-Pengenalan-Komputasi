# Nama : Willy Wilsen
# NIM : 16520145
# Tanggal : 15 November 2020
# Deskripsi : Membuat program yang memeriksa apakah B merupakan anagram dari A

# KAMUS
# A : int
# B : int
# TabA : array (Asumsikan isi array kurang dari 10)
# TabB : array (Asumsikan isi array kurang dari 10)
# i : int(indeks TabA dan TabB)
# frekA : int
# frekB : int
# Asumsikan elemen pada array A dan B max 10

# ALGORITMA
A = int(input("Masukkan banyaknya elemen A: "))
TabA = [0 for i in range(A)] # membuat array A
frekA = [0 for i in range(10)] # membuat array frekuensi A

for i in range(A): # memasukkan isi array A
    TabA[i] = int(input("Masukkan elemen A ke-" + str(i+1) + ": "))
for i in TabA: # menghitung frekuensi A
    frekA[i] += 1

B = int(input("Masukkan banyaknya elemen B: "))
TabB = [0 for i in range(B)] # membuat array B
frekB = [0 for i in range(10)] # membuat array frekuensi B

for i in range(B): # memasukkan isi array B
    TabB[i] = int(input("Masukkan elemen B ke-" + str(i+1) + ": "))
for i in TabB: # menghitung frekuensi B
    frekB[i] += 1
    
# melihat apakah B anagram dari A
if A == B: # jika banyak elemen A sama dengan B
    if frekA == frekB: # dan jika frekuensi A sama dengan B
        print("B adalah anagram dari A")
    else: # jika frekuensi tidak sama
        print("B bukan anagram dari A")
else: # jika banyak elemen tidak sama
    print("B bukan anagram dari A")
