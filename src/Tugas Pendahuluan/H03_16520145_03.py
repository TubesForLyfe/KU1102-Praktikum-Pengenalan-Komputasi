# Nama : Willy Wilsen
# NIM : 16520145
# Tanggal : 15 November 2020
# Deskripsi : Membuat program yang memeriksa apakah sebuah string palindrom

# KAMUS
# x : int
# string : str
# Tab : array
# i : int(indeks Tab)
# palindrom : boolean
# Asumsikan string berisi huruf kecil
# Asumsikan x > 1

# ALGORITMA
x = int(input("Masukkan panjang string: "))
string = str(input("Masukkan string: "))

if len(string) == x: # saat panjang string sesuai
    Tab = list(string) # membuat array dari string 
    i = 0 # untuk indeks pada array Tab
    palindrom = True # inisiasi palindrom

    while i < x: # mengecek palindrom dimulai dari indeks 0
        if Tab[i] != Tab[x-i-1]: # saat tidak palindrom
            palindrom = False
        i += 1 # indeks terus bertambah 1

    if palindrom == True:
        print(string, "adalah palindrom")
    else:
        print(string, "bukan palindrom")
else: # saat panjang string tidak sesuai
    print("Maaf, panjang string tidak sesuai")
