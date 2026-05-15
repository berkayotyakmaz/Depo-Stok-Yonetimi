# Depo Yonetimi - Stok Takip Sistemi

Urun stoklari, satis islemleri ve envanter takibinin yapildigi masaustu uygulamasidir. Tkinter ile koyu temali, yesil accentli modern bir arayuz sunar.

## Teknolojiler

- **Python 3** - Programlama dili
- **Tkinter** - Masaustu GUI framework


## Proje Yapisi

    DepoYonetimi/
    ├── DepoYonetimi.py              # Frontend - Ana arayuz
    ├── DepoYonetimi_Backend.py      # Backend - Is mantigi
    ├── images/                      # Ekran goruntuleri
    └── README.md


## Ana Siniflar

### Urun (`DepoYonetimi_Backend.py`)

- **Ozellikler:** `urun_id`, `ad`, `stok`, `fiyat`
- **Metodlar:** `stok_arttir(miktar)` - stok ekleme, `stok_azalt(miktar)` - stok dusme ve yeterlilik kontrolu


### Siparis (`DepoYonetimi_Backend.py`)

- **Ozellikler:** `siparis_id` (otomatik artan), `urun`, `adet`, `toplam_tutar`
- **Metodlar:** Siparis olusturulurken toplam tutar otomatik hesaplanir (fiyat x adet)


### DepoYonetimi (`DepoYonetimi_Backend.py`)

- **Ozellikler:** `urunler` - urun sozlugu
- **Metodlar:** `get_all_urunler()`, `get_urun_by_id()`, `urun_ekle()`, `satis_yap()`, `stok_ekle()`


### StokApp (`DepoYonetimi.py`)

- **Ozellikler:** Renk paleti, depo yonetimi referansi, liste widget
- **Metodlar:** `arayuz_olustur()`, `stoklari_goster()`, `urun_ekle_penceresi()`, `satis_yap()`, `stok_ekle()`


## Ozellikler

- **Envanter Listesi:** Tum urunlerin ad, stok ve fiyat bilgileriyle listelenmesi
- **Yeni Urun Ekleme:** Ad, stok miktari ve birim fiyat girilerek yeni urun kaydi olusturma
- **Satis Islemi:** Secili urunden 1 adet satis yapma ve stok guncelleme
- **Stok Ekleme:** Secili urune 5 adet stok ekleme
- **Tasarim:** Koyu tema (#091410 arkaplan) + yesil accent (#2ecc71) + modern tipografi


## Ekran Goruntuleri

### Ana Panel

![Ana Panel](images/ana_panel.png)

### Urun Ekleme

![Urun Ekleme](images/urun_ekleme.png)

### Satis Islemi

![Satis Islemi](images/satis_islemi.png)


## Kurulum ve Calistirma

    python DepoYonetimi.py


## Ornek Veri

Ilk calistirmada 6 urun (Elma, Ekmek, Sut, Muz, Cikolata, Su) otomatik olarak yuklenir.
