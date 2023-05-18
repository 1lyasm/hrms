# Ekonomik veriler
bütçe = 1000000
gelir = 800000
gider = 400000
vergi_oranı = 0.2

# Çalışan verileri
çalışanlar = [
    {"isim": "Ahmet", "pozisyon": "Mühendis", "maaş": 5000},
    {"isim": "Mehmet", "pozisyon": "Yazılım Geliştirici", "maaş": 6000},
    {"isim": "Ayşe", "pozisyon": "Proje Yöneticisi", "maaş": 8000},
]

# Otomatik hesaplama
for çalışan in çalışanlar:
    vergi = çalışan["maaş"] * vergi_oranı
    net_maaş = çalışan["maaş"] - vergi
    print(f"{çalışan['isim']}: Brüt maaş: {çalışan['maaş']}, Net maaş: {net_maaş}")

# Maaş ödemeleri
toplam_maaş_maliyeti = sum(çalışan["maaş"] for çalışan in çalışanlar)
kalan_bütçe = gelir - gider
if toplam_maaş_maliyeti <= kalan_bütçe:
    print("Maaşlar ödendi.")
else:
    print("Bütçe yetersiz, maaş ödemeleri yapılamadı.")


