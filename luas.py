import math
import sys

def hitung_luas_lingkaran():
    print("Menghitung luas lingkaran")
    radius = int(input("jari-jari = "))
    luas = 22 / 7 * radius * radius
    print(("Luas= "), luas)


def hitung_luas_persegi_panjang():
    print("Menghitung Luas Persegi Panjang")
    panjang = int(input("panjang= "))
    lebar = int(input("lebar= "))

    luas = panjang * lebar
    print(("Luas="), luas)

def hitung_luas_segitiga():
    print("Menghitung luas Segitiga")
    panjang = int(input("Panjang ="))
    lebar = int(input("Lebar = "))
    tinggi = int(input("Tinggi = "))

    luas = panjang * lebar * tinggi
    print("Luas = ", luas)

def segitiga():
    print("\n---------------------------")
    print(" Menghitung Luas Segitiga")
    print("---------------------------")
    a = int(input("Masukkan alas : "))
    t = int(input("Masukkan tinggi : "))
    luas = 0.5 * a * t
    print("Luas Segitiga : ", luas)
    tanya()

def fibonacci():
    print("\n---------------------------")
    print(" Segitiga Fibonacci")
    print("---------------------------")
    un = int(input("Masukkan suku : "))
    hasil = (un-1)+(un-2)
    print("Hasilnya Adalah :", hasil)
    tanya()

def siku():
    print("\n---------------------------")
    print(" Segitiga Siku-Siku")
    print("---------------------------")
    sisi = input("Sisi yang ingin di cari [a, b, c] : ")
    if sisi == "a":
        b = int(input("Masukkan panjang sisi b : "))
        c = int(input("Masukkan panjang sisi c : "))
        a = math.sqrt((c*c)-(b*b))
        print("Panjang sisi a adalah : " , a)
        tanya()
    elif sisi == 'b':
        a = int(input("Masukkan panjang sisi a : "))
        c = int(input("Masukkan panjang sisi c : "))
        b = math.sqrt((c*c)-(a*a))
        print("Panjang sisi b adalah : " , b)
        tanya()
    elif sisi == 'c':
        a = int(input("Masukkan panjang sisi a : "))
        b = int(input("Masukkan panjang sisi b : "))
        c = math.sqrt((a*a)+(b*b))
        print("Panjang sisi c adalah : " , c)
        tanya()
    else:
        print("\nPilihan yang anda masukkan salah!")
        siku()

# Program Utama
print("Menghitung luas")
print("1. Lingkaran")
print("2. Persegi panjang")
print("3. Segitiga")
print("4. Segitiga Fibonacci")
print("5. Segitiga Siku-Siku")
print("6. Exit")

pilihan = int(input("pilihan(1 , 2 , 3 , 4 , 5 , 6): "))
if pilihan == 1:
    hitung_luas_lingkaran()
elif pilihan == 2:
    hitung_luas_persegi_panjang()
elif pilihan == 3:
    hitung_luas_segitiga()
elif pilihan == 4:
        fibonacci()
elif pilihan == 5:
        siku()
elif pilihan == 6:
        print("Terima kasih sudah menggunakan aplikasi ini!")
        sys.exit()
else:
    print("Pilihan salah")


    def tanya():
        print("\n-----------------------------------------")
        tanya = input(" Ingin mengulang aplikasi lagi? [y/t] : ")
        print("-----------------------------------------")
        if tanya == "y":
            menu()
        elif tanya == "t":
            sys.exit()
        else:
            print("Pilihan yang anda masukan salah!")