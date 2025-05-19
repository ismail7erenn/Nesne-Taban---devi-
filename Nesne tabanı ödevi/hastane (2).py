from datetime import datetime, timedelta

class Hasta:
    def __init__(self, isim, tc):
        self.isim = isim
        self.tc = tc
        self.randevular = []

    def randevu_ekle(self, randevu):
        self.randevular.append(randevu)

    def randevu_sil(self, randevu):
        if randevu in self.randevular:
            self.randevular.remove(randevu)

    def __str__(self):
        return f"{self.isim} - TC: {self.tc}"

class Doktor:
    def __init__(self, isim, uzmanlik):
        self.isim = isim
        self.uzmanlik = uzmanlik
        self.musaitlik = self.otomatik_musaitlik_olustur()

    def otomatik_musaitlik_olustur(self):
        saatler = []
        bugun = datetime.now().date()
        for gun in range(7):
            tarih = bugun + timedelta(days=gun)
            for saat in range(10, 17):
                dt = datetime(tarih.year, tarih.month, tarih.day, saat, 0)
                saatler.append(dt)
        return saatler

    def musait_mi(self, tarih):
        return tarih in self.musaitlik

    def musaitlik_kaldir(self, tarih):
        if tarih in self.musaitlik:
            self.musaitlik.remove(tarih)

    def __str__(self):
        return f"Dr. {self.isim} - Uzmanlık: {self.uzmanlik}"

class Randevu:
    def __init__(self, tarih, doktor, hasta):
        self.tarih = tarih
        self.doktor = doktor
        self.hasta = hasta

    def __str__(self):
        return f"{self.tarih.strftime('%d-%m-%Y %H:%M')} - {self.doktor.isim} ile {self.hasta.isim}"

hastalar = []
doktorlar = []
randevular = []

def hasta_ekle():
    isim = input("Hasta ismi: ")
    tc = input("TC Kimlik No: ")
    hasta = Hasta(isim, tc)
    hastalar.append(hasta)
    print("✅ Hasta eklendi.")

def doktor_ekle():
    isim = input("Doktor ismi: ")
    uzmanlik = input("Uzmanlık alanı: ")
    doktor = Doktor(isim, uzmanlik)
    doktorlar.append(doktor)
    print("✅ Doktor eklendi ve 7 gün boyunca 10:00-17:00 arası müsaitlik tanımlandı.")

def listele_doktorlar():
    print("\n🔍 Doktorlar:")
    for i, d in enumerate(doktorlar):
        print(f"{i}. {d}")

def listele_hastalar():
    print("\n🔍 Hastalar:")
    for i, h in enumerate(hastalar):
        print(f"{i}. {h}")

def randevu_al():
    if not hastalar or not doktorlar:
        print("❌ Önce hasta ve doktor eklemelisiniz.")
        return
    listele_hastalar()
    hasta_index = int(input("Hasta seç (numara): "))
    hasta = hastalar[hasta_index]
    listele_doktorlar()
    doktor_index = int(input("Doktor seç (numara): "))
    doktor = doktorlar[doktor_index]
    print("\n📅 Müsait Saatler:")
    musaitler = doktor.musaitlik
    for i, tarih in enumerate(musaitler):
        print(f"{i}. {tarih.strftime('%d-%m-%Y %H:%M')}")
    if not musaitler:
        print("❌ Bu doktorun şu anda müsaitliği yok.")
        return
    secim = int(input("Tarih seç (numara): "))
    secilen_tarih = musaitler[secim]
    randevu = Randevu(secilen_tarih, doktor, hasta)
    randevular.append(randevu)
    hasta.randevu_ekle(randevu)
    doktor.musaitlik_kaldir(secilen_tarih)
    print("✅ Randevu başarıyla alındı.")

def randevu_iptal():
    listele_hastalar()
    hasta_index = int(input("Hasta seç (numara): "))
    hasta = hastalar[hasta_index]
    if not hasta.randevular:
        print("❌ Bu hastanın randevusu yok.")
        return
    print("📆 Mevcut Randevular:")
    for i, r in enumerate(hasta.randevular):
        print(f"{i}. {r}")
    r_index = int(input("İptal edilecek randevu (numara): "))
    randevu = hasta.randevular[r_index]
    hasta.randevu_sil(randevu)
    randevular.remove(randevu)
    randevu.doktor.musaitlik.append(randevu.tarih)
    print("✅ Randevu iptal edildi.")

def randevulari_goster():
    print("\n📋 Tüm Randevular:")
    if not randevular:
        print("🔍 Henüz randevu alınmamış.")
    for r in randevular:
        print(r)

def ana_menu():
    while True:
        print("\n--- 🏥 Hastane Randevu Sistemi ---")
        print("1. Hasta Ekle")
        print("2. Doktor Ekle")
        print("3. Randevu Al")
        print("4. Randevu İptal Et")
        print("5. Randevuları Göster")
        print("6. Çıkış")
        secim = input("Seçiminiz: ")
        if secim == "1":
            hasta_ekle()
        elif secim == "2":
            doktor_ekle()
        elif secim == "3":
            randevu_al()
        elif secim == "4":
            randevu_iptal()
        elif secim == "5":
            randevulari_goster()
        elif secim == "6":
            print("" \
            " Sistemden çıkılıyor...")
            break
        else:
            print("❌ Geçersiz seçim. Tekrar deneyin.")

if __name__ == "__main__":
    ana_menu()
    
