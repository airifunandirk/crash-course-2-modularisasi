"""
Program menghitung luas segitiga
luas segitiga = alas * tinggi/2
"""

print("Menghitung luas segitiga 1")
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f"Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}")


print("Menghitung luas segitiga 2")
alas = 15
tinggi = 7
luas_segitiga = alas * tinggi / 2
print(f"Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}")

print("Membuat Fungsi hitung_luas_segitiga")
def hitung_luas_segitiga(alas,tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f"Menghitung luas segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(10,6)}")
print(f"Menghitung luas segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(15,7)}")

