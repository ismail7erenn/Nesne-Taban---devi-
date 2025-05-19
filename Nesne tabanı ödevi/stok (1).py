class Urun:
    def __init__(self, ad, stok_miktari):
        self.ad = ad
        self.stok_miktari = stok_miktari

    def stok_guncelle(self, miktar):
        self.stok_miktari += miktar

    def siparis_olustur(self, miktar):
        if self.stok_miktari >= miktar:
            self.stok_miktari -= miktar
            return True
        else:
            return False

    def __str__(self):
        return f"{self.ad} - Stok: {self.stok_miktari}"


class Siparis:
    siparis_sayac = 1

    def __init__(self, urun_adi, miktar):
        self.siparis_no = Siparis.siparis_sayac
        Siparis.siparis_sayac += 1
        self.urun_adi = urun_adi
        self.miktar = miktar

    def __str__(self):
        return f"Sipariş #{self.siparis_no} - Ürün: {self.urun_adi} - Adet: {self.miktar}"


def stok_listesini_goster(urunler):
    print("\n📦 Mevcut Stok Listesi:")
    for urun in urunler:
        print(urun)
    print()


def main():
    print("📦 Stok Takip Sistemine Hoş Geldiniz!\n")
    urunler = []

    while True:
        print("\nMenü:")
        print("1 - Ürün Ekle")
        print("2 - Stok Güncelle")
        print("3 - Sipariş Oluştur")
        print("4 - Stokları Görüntüle")
        print("5 - Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            ad = input("Ürün adı: ")
            stok = int(input("Başlangıç stok miktarı: "))
            urunler.append(Urun(ad, stok))
            print(f"{ad} ürünü eklendi.")
        
        elif secim == "2":
            stok_listesini_goster(urunler)
            ad = input("Stok güncellenecek ürün adı: ")
            miktar = int(input("Eklemek istediğiniz stok miktarı: "))
            bulundu = False
            for urun in urunler:
                if urun.ad == ad:
                    urun.stok_guncelle(miktar)
                    print("Stok güncellendi.")
                    bulundu = True
            if not bulundu:
                print("Ürün bulunamadı.")

        elif secim == "3":
            stok_listesini_goster(urunler)
            ad = input("Sipariş verilecek ürün adı: ")
            miktar = int(input("Sipariş miktarı: "))
            bulundu = False
            for urun in urunler:
                if urun.ad == ad:
                    if urun.siparis_olustur(miktar):
                        siparis = Siparis(ad, miktar)
                        print(f"Sipariş oluşturuldu: {siparis}")
                    else:
                        print("Yetersiz stok!")
                    bulundu = True
            if not bulundu:
                print("Ürün bulunamadı.")

        elif secim == "4":
            stok_listesini_goster(urunler)

        elif secim == "5":
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()