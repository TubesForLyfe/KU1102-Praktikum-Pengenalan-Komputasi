# Nama : Willy Wilsen
# NIM : 16520145
# Tanggal : 16 Oktober 2020
# Deskripsi : Membuat program kalkulator sederhana

# KAMUS
# a : integer
# b : integer
# operator : str

# ALGORITMA
a = int(input("Masukkan a: "))
b = int(input("Masukkan b: "))
operator = str(input("Masukan operator: "))

if (operator == "+"):
    print(a, "+", b, "=", (a+b))
elif (operator == "-"):
    print(a, "-", b, "=", (a-b))
elif (operator == "*"):
    print(a, "*", b, "=", (a*b))
elif (operator == "/"):
    print(a, "/", b, "=", (a//b))
else:
    print("Operator tidak sesuai")
