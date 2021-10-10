# Nama : Willy Wilsen
# NIM : 16520145
# Tanggal : 18 November 2020
# Deskripsi : Membuat program  semua pelat nomor mobil Tuan Mor dan banyak mobil yang diterima masing-masing anaknya.

# KAMUS
# M : int (Asumsikan lebih dari 0)
# N : int (Asumsikan lebih dari 0)
# TabM : array
# frekM : array
# i : int(indeks array)

# ALGORITMA
M = int(input("Masukkan M: ")) # input banyaknya mobil
TabM = [0 for i in range(M)] # membuat array pelat mobil

for i in range(M): # menginput pelat mobil Tuan Mor
    TabM[i] = int(input("Masukkan pelat nomor mobil ke-" + str(i+1) + ": "))

N = int(input("Masukkan N: ")) # input jumlah anak
frekM = [0 for i in range(N)] # membuat array frekuensi sisa bagi pelat mobil
for i in range(M): 
    TabM[i] = TabM[i] % N # sisa bagi pelat mobil dengan jumlah anaknya
for i in TabM:
    frekM[i] += 1 # frekuensi bertambah

i = 0
while i < N: # Anak ke-i mendapatkan banyak mobil sesuai jumlah frekuensi
    print("Anak ke-" + str(i+1), "mendapatkan", frekM[i], "mobil")
    i += 1 # agar output setiap anak keluar
