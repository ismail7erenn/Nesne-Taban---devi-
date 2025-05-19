class Kitap:
    def __init__(self, kitap_id, ad, yazar):
        self.kitap_id = kitap_id
        self.ad = ad
        self.yazar = yazar
        self.odunc_alindi = False

    def durum_guncelle(self, odunc_mu):
        self.odunc_alindi = odunc_mu

    def __str__(self):
        durum = "Mevcut" if not self.odunc_alindi else "Ödünç Alındı"
        return f"{self.kitap_id} - {self.ad} - {self.yazar} ({durum})"

class Uye:
    def __init__(self, uye_id, ad):
        self.uye_id = uye_id
        self.ad = ad
        self.odunc_kitaplar = []

    def kitap_ekle(self, kitap):
        self.odunc_kitaplar.append(kitap)

    def kitap_iade(self, kitap):
        if kitap in self.odunc_kitaplar:
            self.odunc_kitaplar.remove(kitap)

    def __str__(self):
        return f"{self.uye_id} - {self.ad}"

class Odunc:
    def __init__(self, kitap, uye):
        self.kitap = kitap
        self.uye = uye

    def odunc_al(self):
        if not self.kitap.odunc_alindi:
            self.kitap.durum_guncelle(True)
            self.uye.kitap_ekle(self.kitap)
            print(f"✅ Kitap '{self.kitap.ad}' ödünç verildi.")
        else:
            print("❌ Bu kitap zaten ödünç alınmış.")

    def iade_et(self):
        if self.kitap.odunc_alindi:
            self.kitap.durum_guncelle(False)
            self.uye.kitap_iade(self.kitap)
            print(f"✅ Kitap '{self.kitap.ad}' iade edildi.")
        else:
            print("❌ Bu kitap zaten kütüphanede mevcut.")

# Veri yapıları
kitaplar = []
uyeler = []

# Fonksiyonlar
def kitap_ekle():
    kitap_id = input("Kitap ID: ")
    ad = input("Kitap Adı: ")
    yazar = input("Yazar: ")
    kitap = Kitap(kitap_id, ad, yazar)
    kitaplar.append(kitap)
    print("✅ Kitap eklendi.")

def kitap_ara():
    aranan = input("Kitap adını girin: ").strip().lower()
    bulunan = [k for k in kitaplar if k.ad.strip().lower() == aranan]
    if bulunan:
        print("🔍 Bulunan Kitaplar:")
        for kitap in bulunan:
            print(kitap)
    else:
        print("❌ Kitap bulunamadı.")

def uye_ekle():
    uye_id = input("Üye ID: ")
    ad = input("Üye Adı: ")
    uye = Uye(uye_id, ad)
    uyeler.append(uye)
    print("✅ Üye eklendi.")

def odunc_al():
    if not kitaplar or not uyeler:
        print("❗ Önce kitap ve üye ekleyin.")
        return
    kitap_ara()
    kitap_id = input("Ödünç alınacak kitap ID: ")
    kitap = next((k for k in kitaplar if k.kitap_id == kitap_id), None)
    if not kitap:
        print("❌ Kitap ID bulunamadı.")
        return
    print("📚 Üyeler:")
    for i, uye in enumerate(uyeler):
        print(f"{i}. {uye}")
    uye_index = int(input("Üye seç (numara): "))
    uye = uyeler[uye_index]
    odunc = Odunc(kitap, uye)
    odunc.odunc_al()

def kitap_iade():
    kitap_id = input("İade edilecek kitap ID: ")
    kitap = next((k for k in kitaplar if k.kitap_id == kitap_id), None)
    if not kitap:
        print("❌ Kitap ID bulunamadı.")
        return
    uye = next((u for u in uyeler if kitap in u.odunc_kitaplar), None)
    if not uye:
        print("❌ Bu kitap hiçbir üyede kayıtlı değil.")
        return
    odunc = Odunc(kitap, uye)
    odunc.iade_et()

def tum_kitaplari_goster():
    if not kitaplar:
        print("❗ Kütüphanede hiç kitap yok.")
    else:
        print("📚 Tüm Kitaplar:")
        for kitap in kitaplar:
            print(kitap)

# Ana Menü
def ana_menu():
    while True:
        print("\n--- 📖 Kütüphane Yönetim Sistemi ---")
        print("1. Kitap Ekle")
        print("2. Kitap Ara")
        print("3. Üye Ekle")
        print("4. Kitap Ödünç Al")
        print("5. Kitap İade Et")
        print("6. Tüm Kitapları Göster")
        print("7. Çıkış")
        secim = input("Seçiminiz: ")
        if secim == "1":
            kitap_ekle()
        elif secim == "2":
            kitap_ara()
        elif secim == "3":
            uye_ekle()
        elif secim == "4":
            odunc_al()
        elif secim == "5":
            kitap_iade()
        elif secim == "6":
            tum_kitaplari_goster()
        elif secim == "7":
            print("👋 Sistemden çıkılıyor...")
            break
        else:
            print("❌ Geçersiz seçim. Tekrar deneyin.")

if __name__ == "__main__":
    ana_menu()
