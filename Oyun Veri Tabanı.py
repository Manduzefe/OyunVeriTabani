import tkinter as tk
from tkinter import messagebox, Scrollbar

class Oyun:
    def __init__(self, ad, tur, platform):
        self.ad = ad
        self.tur = tur
        self.platform = platform
        self.degerlendirme = []

    def oyun_ekle(self):
        return f"{self.ad} ({self.tur} - {self.platform}) eklendi."

    def değerlendir(self, puan):
        self.degerlendirme.append(puan)

    def ortalama_puan(self):
        return sum(self.degerlendirme) / len(self.degerlendirme) if self.degerlendirme else 0

    def __str__(self):
        return f"{self.ad} ({self.tur}) - {self.platform} | Ortalama Puan: {self.ortalama_puan():.1f}"

class Koleksiyon:
    def __init__(self):
        self.oyunlar = []

    def oyun_ekle(self, oyun):
        self.oyunlar.append(oyun)

    def oyun_sil(self, oyun):
        if oyun in self.oyunlar:
            self.oyunlar.remove(oyun)

    def listele(self):
        return [str(oyun) for oyun in self.oyunlar]

class Oyuncu:
    def __init__(self, ad):
        self.ad = ad
        self.koleksiyon = Koleksiyon()

    def favorilere_ekle(self, oyun):
        if oyun not in self.koleksiyon.oyunlar:
            self.koleksiyon.oyun_ekle(oyun)

    def oyun_oner(self, tur):
        return [oyun for oyun in self.koleksiyon.oyunlar if oyun.tur == tur]

class OyunArayuz:
    def __init__(self, oyuncu):
        self.oyuncu = oyuncu
        self.pencere = tk.Tk()
        self.pencere.title("Oyun Koleksiyonu")

        self.frame = tk.Frame(self.pencere)
        self.frame.pack(padx=10, pady=10)

        self.scroll_x = Scrollbar(self.frame, orient="horizontal")
        self.scroll_y = Scrollbar(self.frame, orient="vertical")
        self.listbox = tk.Listbox(self.frame, width=60, height=10, xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.scroll_x.config(command=self.listbox.xview)
        self.scroll_y.config(command=self.listbox.yview)
        self.listbox.grid(row=0, column=0)
        self.scroll_y.grid(row=0, column=1, sticky='ns')
        self.scroll_x.grid(row=1, column=0, sticky='we')

        tk.Label(self.pencere, text="Oyun Adı:").pack()
        self.entry_ad = tk.Entry(self.pencere)
        self.entry_ad.pack(pady=2)

        tk.Label(self.pencere, text="Oyun Türü:").pack()
        self.entry_tur = tk.Entry(self.pencere)
        self.entry_tur.pack(pady=2)

        tk.Label(self.pencere, text="Platform:").pack()
        self.entry_platform = tk.Entry(self.pencere)
        self.entry_platform.pack(pady=2)

        tk.Label(self.pencere, text="Puan (0-10):").pack()
        self.entry_puan = tk.Entry(self.pencere)
        self.entry_puan.pack(pady=2)

        self.btn_ekle = tk.Button(self.pencere, text="Oyun Ekle", command=self.kullanici_girdisi_ile_ekle)
        self.btn_ekle.pack(pady=5)

        self.btn_sil = tk.Button(self.pencere, text="Seçiliyi Sil", command=self.koleksiyondan_sil)
        self.btn_sil.pack(pady=5)

        self.btn_goster = tk.Button(self.pencere, text="Koleksiyonu Göster", command=self.koleksiyonu_goster)
        self.btn_goster.pack(pady=5)

        self.guncelle_listbox()
        self.pencere.mainloop()

    def guncelle_listbox(self):
        self.listbox.delete(0, tk.END)
        for oyun in self.oyuncu.koleksiyon.oyunlar:
            self.listbox.insert(tk.END, str(oyun))

    def kullanici_girdisi_ile_ekle(self):
        ad = self.entry_ad.get()
        tur = self.entry_tur.get()
        platform = self.entry_platform.get()
        puan_str = self.entry_puan.get()
        if ad and tur and platform:
            try:
                puan = float(puan_str)
                if puan < 0 or puan > 10:
                    raise ValueError
            except ValueError:
                messagebox.showwarning("Hata", "Lütfen 0 ile 10 arasında bir puan girin!")
                return
            yeni_oyun = Oyun(ad, tur, platform)
            yeni_oyun.değerlendir(puan)
            self.oyuncu.koleksiyon.oyun_ekle(yeni_oyun)
            messagebox.showinfo("Başarılı", f"{yeni_oyun.ad} koleksiyona eklendi!")
            self.guncelle_listbox()
        else:
            messagebox.showwarning("Hata", "Lütfen tüm bilgileri girin!")

    def koleksiyondan_sil(self):
        secilen_index = self.listbox.curselection()
        if secilen_index:
            secilen_oyun = self.oyuncu.koleksiyon.oyunlar[secilen_index[0]]
            self.oyuncu.koleksiyon.oyun_sil(secilen_oyun)
            messagebox.showinfo("Silindi", f"{secilen_oyun.ad} koleksiyondan silindi!")
            self.guncelle_listbox()
        else:
            messagebox.showwarning("Hata", "Lütfen bir oyun seçin!")

    def koleksiyonu_goster(self):
        oyunlar = self.oyuncu.koleksiyon.listele()
        if oyunlar:
            messagebox.showinfo("Koleksiyon", "\n".join(oyunlar))
        else:
            messagebox.showinfo("Koleksiyon", "Henüz koleksiyona oyun eklenmemiş.")
            
if __name__ == "__main__":
    oyuncu = Oyuncu("Efe")
    arayuz = OyunArayuz(oyuncu)
