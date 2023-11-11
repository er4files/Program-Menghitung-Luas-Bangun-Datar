import math

def hitung_luas_persegi(sisi):
    return sisi * sisi

def hitung_keliling_persegi(sisi):
    return 4 * sisi

def hitung_luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def hitung_keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def hitung_luas_lingkaran(jari_jari):
    return math.pi * jari_jari ** 2

def hitung_keliling_lingkaran(jari_jari):
    return 2 * math.pi * jari_jari

def hitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def hitung_keliling_segitiga(sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

def cetak_hasil(nama_bangun, luas, keliling):
    print(f"\n=== {nama_bangun} ===")
    print(f"Luas: {luas}")
    print(f"Keliling: {keliling}")
    print("=========================")

# Bingkai judul program
print("===============================")
print("PROGRAM MENGHITUNG LUAS BANGUN DATAR")
print("===============================")

# Memilih bangun datar
print("Pilih bangun datar yang ingin dihitung:")
print("1. Persegi")
print("2. Persegi Panjang")
print("3. Lingkaran")
print("4. Segitiga")

pilihan = input("Masukkan nomor pilihan (1-4): ")

# Memasukkan nilai sesuai dengan pilihan
if pilihan == '1':
    sisi_persegi = float(input("Masukkan panjang sisi persegi: "))
    luas = hitung_luas_persegi(sisi_persegi)
    keliling = hitung_keliling_persegi(sisi_persegi)
    cetak_hasil("Persegi", luas, keliling)

elif pilihan == '2':
    panjang_persegi_panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar_persegi_panjang = float(input("Masukkan lebar persegi panjang: "))
    luas = hitung_luas_persegi_panjang(panjang_persegi_panjang, lebar_persegi_panjang)
    keliling = hitung_keliling_persegi_panjang(panjang_persegi_panjang, lebar_persegi_panjang)
    cetak_hasil("Persegi Panjang", luas, keliling)

elif pilihan == '3':
    jari_jari_lingkaran = float(input("Masukkan jari-jari lingkaran: "))
    luas = hitung_luas_lingkaran(jari_jari_lingkaran)
    keliling = hitung_keliling_lingkaran(jari_jari_lingkaran)
    cetak_hasil("Lingkaran", luas, keliling)

elif pilihan == '4':
    alas_segitiga = float(input("Masukkan alas segitiga: "))
    tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
    sisi1_segitiga = float(input("Masukkan sisi pertama segitiga: "))
    sisi2_segitiga = float(input("Masukkan sisi kedua segitiga: "))
    sisi3_segitiga = float(input("Masukkan sisi ketiga segitiga: "))
    luas = hitung_luas_segitiga(alas_segitiga, tinggi_segitiga)
    keliling = hitung_keliling_segitiga(sisi1_segitiga, sisi2_segitiga, sisi3_segitiga)
    cetak_hasil("Segitiga", luas, keliling)

else:
    print("Pilihan tidak valid.")
