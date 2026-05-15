# backend.py

class Urun:
    def __init__(self, urun_id, ad, stok, fiyat):
        self.urun_id = urun_id
        self.ad = ad
        self.stok = stok
        self.fiyat = fiyat

    def stok_arttir(self, miktar):
        self.stok += miktar

    def stok_azalt(self, miktar):
        if self.stok >= miktar:
            self.stok -= miktar
            return True
        return False

class Siparis:
    sayac = 1
    def __init__(self, urun, adet):
        self.siparis_id = Siparis.sayac
        Siparis.sayac += 1
        self.urun = urun
        self.adet = adet
        self.toplam_tutar = urun.fiyat * adet

class DepoYonetimi:
    def __init__(self):
        # Başlangıç ürünleri burada yönetilir
        self.urunler = {
            "1": Urun("1", "Elma", 50, 5.5),
            "2": Urun("2", "Ekmek", 20, 10.0),
            "3": Urun("3", "Süt", 15, 25.0),
            "4": Urun("4", "Muz", 30, 18.0),
            "5": Urun("5", "Çikolata", 45, 12.0),
            "6": Urun("6", "Su", 100, 5.0)
        }

    def get_all_urunler(self):
        """Depodaki tüm ürünlerin listesini döner."""
        return list(self.urunler.values())

    def get_urun_by_id(self, urun_id):
        """Belirtilen ID'ye sahip ürünü döner. Bulunamazsa None döner."""
        return self.urunler.get(urun_id)

    def urun_ekle(self, ad, stok, fiyat):
        """
        Yeni bir ürün oluşturur ve depoya ekler.
        Yeni ürün ID'si mevcut ürün sayısına göre otomatik olarak atanır.
        """
        # Mevcut ürün sayısına göre yeni bir ID oluştur.
        yeni_id = str(len(self.urunler) + 1)
        yeni_urun = Urun(yeni_id, ad, stok, fiyat)
        self.urunler[yeni_id] = yeni_urun
        return True

    def satis_yap(self, urun_id, miktar=1):
        """
        Belirtilen ID'ye sahip üründen belirli miktarda satış yapar.
        Ürün bulunamazsa veya stok yetersizse False döner, aksi takdirde True döner.
        """
        urun = self.get_urun_by_id(urun_id)
        if urun:
            # Urun nesnesinin stok_azalt metodunu çağırarak stok güncellemesini yapar.
            return urun.stok_azalt(miktar)
        return False

    def stok_ekle(self, urun_id, miktar=5):
        """
        Belirtilen ID'ye sahip ürüne belirli miktarda stok ekler.
        Ürün bulunamazsa False döner, aksi takdirde True döner.
        """
        urun = self.get_urun_by_id(urun_id)
        if urun:
            # Urun nesnesinin stok_arttir metodunu çağırarak stok güncellemesini yapar.
            urun.stok_arttir(miktar)
            return True
        return False