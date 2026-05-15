# frontend.py

import tkinter as tk
from tkinter import ttk, messagebox
from DepoYonetimi_Backend import DepoYonetimi

class StokApp(tk.Tk):
    """
    Uygulamanın ana penceresini ve tüm GUI bileşenlerini yöneten sınıf.
    Backend ile etkileşimi sağlar ve kullanıcı arayüzünü günceller.
    """
    def __init__(self):
        super().__init__()
        self.title("Warehouse & Stock Dashboard")
        self.geometry("900x600")
        self.configure(bg="#091410")

        # Renk Paleti
        self.bg_color = "#091410"
        self.card_color = "#11221a"
        self.accent_color = "#2ecc71"
        self.text_color = "#ffffff"

        # Backend iş mantığını yöneten DepoYonetimi sınıfının bir örneğini oluştur.
        self.depo_yonetimi = DepoYonetimi()

        # Kullanıcı arayüzünü oluşturma metodunu çağır.
        self.arayuz_olustur()

    def arayuz_olustur(self):
        """Uygulamanın ana arayüz bileşenlerini (header, listeler, butonlar vb.) oluşturur."""
        # Başlık (Header) alanı
        header = tk.Frame(self, bg=self.bg_color, padx=20, pady=20)
        header.pack(fill="x")
        tk.Label(header, text="STOCK PANEL", font=("Segoe UI", 24, "bold"), fg=self.text_color, bg=self.bg_color).pack(side="left")
        tk.Label(header, text="Depo & Stok Yönetimi — Envanter Durumu", font=("Segoe UI", 10), fg="#5d7a6d", bg=self.bg_color).place(x=5, y=45)

        # Ana içerik alanı (Main Container)
        main_container = tk.Frame(self, bg=self.bg_color)
        main_container.pack(fill="both", expand=True, padx=20)

        # Envanter Listesi Kartı
        # Bu kart, mevcut ürünlerin listesini ve detaylarını gösterir.
        list_card = tk.Frame(main_container, bg=self.card_color, padx=20, pady=20, highlightthickness=1, highlightbackground="#1d3d2e")
        list_card.place(relx=0, rely=0, relwidth=0.6, relheight=0.9)

        tk.Label(list_card, text="MEVCUT ENVANTER", font=("Segoe UI", 12, "bold"), fg=self.accent_color, bg=self.card_color).pack(anchor="w", pady=(0,20))

        # Ürünlerin listelendiği Listbox widget'ı
        self.liste = tk.Listbox(list_card, bg="#091410", fg="#bdc3c7", borderwidth=0, font=("Segoe UI", 11), highlightthickness=1, highlightbackground="#1d3d2e", selectbackground=self.accent_color)
        self.liste.pack(fill="both", expand=True, pady=(0,10))
        self.stoklari_goster()

        # İşlem Paneli Kartı (Sağ)
        action_card = tk.Frame(main_container, bg=self.card_color, padx=20, pady=20, highlightthickness=1, highlightbackground="#1d3d2e")
        action_card.place(relx=0.65, rely=0, relwidth=0.35, relheight=0.9)

        # İşlem paneli başlığı
        tk.Label(action_card, text="HIZLI İŞLEMLER", font=("Segoe UI", 12, "bold"), fg="#f1c40f", bg=self.card_color).pack(anchor="w", pady=(0,20))

        # Yeni ürün ekleme butonu
        tk.Button(action_card, text="YENİ ÜRÜN EKLE", command=self.urun_ekle_penceresi, bg="#3498db", fg="white", font=("Segoe UI", 10, "bold"), borderwidth=0, cursor="hand2", pady=15).pack(fill="x", pady=10)
        # Seçili ürünü satma butonu
        tk.Button(action_card, text="SEÇİLİ ÜRÜNÜ SAT (1)", command=self.satis_yap, bg="#e67e22", fg="white", font=("Segoe UI", 10, "bold"), borderwidth=0, cursor="hand2", pady=15).pack(fill="x", pady=10)
        # Seçili ürüne stok ekleme butonu
        tk.Button(action_card, text="STOK EKLE (+5)", command=self.stok_ekle, bg="#27ae60", fg="white", font=("Segoe UI", 10, "bold"), borderwidth=0, cursor="hand2", pady=15).pack(fill="x", pady=10)

        # Alt Bilgi Alanı
        tk.Label(action_card, text="* Lütfen işlem yapmak istediğiniz\n ürünü listeden seçiniz.", fg="#5d7a6d", bg=self.card_color, font=("Segoe UI", 9, "italic")).pack(pady=20)

    def stoklari_goster(self):
        """
        Backend'den güncel ürün listesini alır ve Listbox widget'ında görüntüler.
        """
        self.liste.delete(0, tk.END)
        # Backend'den ürünleri al
        for u in self.depo_yonetimi.get_all_urunler():
            self.liste.insert(tk.END, f"📦 {u.ad.ljust(15)} | Stok: {str(u.stok).zfill(2)} | Fiyat: {u.fiyat} TL")

    def urun_ekle_penceresi(self):
        pencere = tk.Toplevel(self)
        pencere.title("Yeni Ürün Ekle")
        pencere.geometry("300x400")
        pencere.configure(bg=self.card_color)

        tk.Label(pencere, text="Ürün Adı:", fg=self.text_color, bg=self.card_color, font=("Segoe UI", 10)).pack(pady=(20, 5))
        ent_ad = tk.Entry(pencere)
        ent_ad.pack(pady=5)

        tk.Label(pencere, text="Stok Miktarı:", fg=self.text_color, bg=self.card_color, font=("Segoe UI", 10)).pack(pady=5)
        ent_stok = tk.Entry(pencere)
        ent_stok.pack(pady=5)

        tk.Label(pencere, text="Birim Fiyat (TL):", fg=self.text_color, bg=self.card_color, font=("Segoe UI", 10)).pack(pady=5)
        ent_fiyat = tk.Entry(pencere)
        ent_fiyat.pack(pady=5)

        def kaydet():
            ad = ent_ad.get()
            try:
                stok = int(ent_stok.get())
                fiyat = float(ent_fiyat.get())
                if ad:
                    self.depo_yonetimi.urun_ekle(ad, stok, fiyat)
                    self.stoklari_goster()
                    pencere.destroy()
                    messagebox.showinfo("Başarılı", f"{ad} envantere eklendi.")
                else:
                    messagebox.showwarning("Eksik Bilgi", "Lütfen ürün adını girin.")
            except ValueError:
                messagebox.showerror("Hata", "Stok ve fiyat için geçerli sayılar girin!")

        # Kaydet butonu
        tk.Button(pencere, text="KAYDET", command=kaydet, bg=self.accent_color, fg="white", font=("Segoe UI", 10, "bold"), pady=10, width=15).pack(pady=30)

    def satis_yap(self):
        """
        Listbox'ta seçili olan üründen 1 adet satış yapar.
        İşlemi backend üzerinden gerçekleştirir ve sonucu kullanıcıya bildirir.
        """
        secili = self.liste.curselection()
        if secili:
            # Listbox'taki seçimin indeksini kullanarak ürün ID'sini alıyoruz.
            # Bu yöntem, ürünlerin listbox'a eklenme sırasına bağımlıdır.
            # Daha sağlam bir yaklaşım için, listbox'a ürün ID'lerini de kaydetmek düşünülebilir.
            urun_id = str(secili[0] + 1)
            urun = self.depo_yonetimi.get_urun_by_id(urun_id)
            # Backend'deki satis_yap metodunu çağırır.
            if urun:
                if self.depo_yonetimi.satis_yap(urun_id, 1): # Backend üzerinden satış yap
                    self.stoklari_goster()
                    messagebox.showinfo("Satış", f"{urun.ad} başarıyla satıldı.")
                else:
                    messagebox.showwarning("Yetersiz", "Stokta ürün kalmadı!")
            else:
                messagebox.showwarning("Hata", "Ürün bulunamadı!")
        else:
            messagebox.showwarning("Seçim Yapın", "Lütfen listeden bir ürün seçin.")

    def stok_ekle(self):
        """
        Listbox'ta seçili olan ürüne 5 adet stok ekler.
        İşlemi backend üzerinden gerçekleştirir ve sonucu kullanıcıya bildirir.
        """
        secili = self.liste.curselection()
        if secili:
            urun_id = str(secili[0] + 1)
            urun = self.depo_yonetimi.get_urun_by_id(urun_id)
            # Backend'deki stok_ekle metodunu çağırır.
            if urun:
                if self.depo_yonetimi.stok_ekle(urun_id, 5): # Backend üzerinden stok ekle
                    self.stoklari_goster()
                    messagebox.showinfo("Güncellendi", f"{urun.ad} stoğu artırıldı.")
                else:
                    messagebox.showwarning("Hata", "Stok eklenirken bir sorun oluştu.")
            else:
                messagebox.showwarning("Hata", "Ürün bulunamadı!")
        else:
            messagebox.showwarning("Seçim Yapın", "Lütfen listeden bir ürün seçin.")

if __name__ == "__main__":
    # Uygulama doğrudan çalıştırıldığında ana pencereyi oluşturur ve başlatır.
    app = StokApp()
    app.mainloop()