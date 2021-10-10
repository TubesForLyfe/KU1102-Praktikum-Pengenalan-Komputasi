# Nama : Willy Wilsen
# NIM : 16520145
# Tanggal : 29 November 2020
# Deskripsi : Membuat program yang menuliskan semua nilai dari f(A) hingga f(B)

# KAMUS
# A : int
# B : int
# f(x) : fungsi
# i : int

# ALGORITMA
A = int(input("Masukkan A: ")) # input A
B = int(input("Masukkan B: ")) # input B

def f(x): # membuat fungsi f(x)
    fx = x**2 - 2*x + 5
    return fx # mengembalikan nilai f(x)

for i in range(A,B+1): # looping f(A) hingga f(B)
    print("f(" + str(i) + ") =", f(i)) # print fungsi tersebut
