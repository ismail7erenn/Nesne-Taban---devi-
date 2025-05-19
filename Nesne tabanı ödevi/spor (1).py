class Sporcu:
    def __init__(self, ad, spor_dali):
        self.ad = ad
        self.spor_dali = spor_dali
        self.antrenman_programi = []
        self.ilerleme_kaydi = []

    def program_olustur(self, antrenman):
        self.antrenman_programi.append(antrenman)

    def ilerleme_kaydet(self, takip):
        self.ilerleme_kaydi.append(takip)

    def rapor_al(self):
        print(f"\n--- {self.ad} için Antrenman Raporu ---")
        if not self.ilerleme_kaydi:
            print("Henüz bir ilerleme kaydı yok.")
        else:
            for kayit in self.ilerleme_kaydi:
                print(kayit)
        print("--- Rapor Sonu ---\n")


class Antrenman:
    def __init__(self, ad, detay):
        self.ad = ad
        self.detay = detay

    def __str__(self):
        return f"{self.ad}: {self.detay}"


class Takip:
    def __init__(self, tarih, antrenman_adi, aciklama):
        self.tarih = tarih
        self.antrenman_adi = antrenman_adi
        self.aciklama = aciklama

    def __str__(self):
        return f"{self.tarih} - {self.antrenman_adi}: {self.aciklama}"


def main():
    print("🏋️ Spor Takip Uygulamasına Hoş Geldiniz!\n")

    ad = input("Sporcunun adını girin: ")
    spor_dali = input("Spor dalını girin: ")
    sporcu = Sporcu(ad, spor_dali)

    while True:
        cevap = input("Yeni bir antrenman eklemek ister misiniz? (e/h): ").lower()
        if cevap == "h":
            break
        ant_ad = input("Antrenman adı: ")
        ant_detay = input("Antrenman detayı: ")
        antrenman = Antrenman(ant_ad, ant_detay)
        sporcu.program_olustur(antrenman)

    while True:
        cevap = input("Yeni bir ilerleme kaydı eklemek ister misiniz? (e/h): ").lower()
        if cevap == "h":
            break
        tarih = input("Tarih (GG-AA-YYYY): ")
        ant_adi = input("Antrenman adı: ")
        aciklama = input("Açıklama: ")
        takip = Takip(tarih, ant_adi, aciklama)
        sporcu.ilerleme_kaydet(takip)

    sporcu.rapor_al()


if __name__ == "__main__":
    main()
