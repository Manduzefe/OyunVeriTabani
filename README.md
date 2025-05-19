# Oyun Koleksiyonu Uygulaması - Kullanıcı ve Geliştirici Dokümantasyonu

## 📌 Proje Tanımı
Bu uygulama, bir oyuncunun sahip olduğu oyunları sistematik bir şekilde kaydetmesini ve yönetmesini sağlar. Kullanıcılar arayüz üzerinden oyun adı, türü, platformu ve puan bilgisi girerek kendi koleksiyonlarını oluşturabilir.

Bu Proje Python dilinde geliştirilmiştir ve `tkinter` arayüz kütüphanesi ile görselleştirilmiştir.

---

## 🧱 Uygulama Mimarisi

### 🎮 Oyun (`Oyun` Sınıfı)
Bir oyunu temsil eder.

- `ad`: Oyun adı (string)
- `tur`: Tür (örneğin: Aksiyon, RPG, Strateji)
- `platform`: Oyun platformu (örneğin: PC, PS, Xbox)
- `degerlendirme`: Kullanıcı puanlarını tutar (liste)

**Fonksiyonlar:**
- `değerlendir(puan)`: Oyuna puan ekler
- `ortalama_puan()`: Ortalama puanı döndürür
- `__str__()`: Oyun bilgilerini yazıya çevirir

---

### 📚 Koleksiyon (`Koleksiyon` Sınıfı)
Kullanıcının sahip olduğu oyunları saklar.

- `oyunlar`: Oyun objelerinden oluşan liste

**Fonksiyonlar:**
- `oyun_ekle(oyun)`
- `oyun_sil(oyun)`
- `listele()`: Tüm oyunları listeler

---

### 👤 Oyuncu (`Oyuncu` Sınıfı)
Uygulamayı kullanan kişiyi temsil eder.

- `ad`: Oyuncu adı
- `koleksiyon`: Oyun Koleksiyonu objesi

**Fonksiyonlar:**
- `favorilere_ekle(oyun)`
- `oyun_oner(tur)`: Belirtilen türe göre öneri sunar

---

## 💻 Arayüz (arayuz.py)

`tkinter` kütüphanesi ile tasarlanmıştır.

**Kullanıcı Giriş Alanları:**
- Oyun Adı
- Oyun Türü
- Platform
- Puan (0-10 arası)

**Butonlar:**
- 🟩 `Oyun Ekle`: Girdileri alır, koleksiyona ekler.
- 🗑️ `Seçiliyi Sil`: Listeden seçilen oyunu siler.
- 📋 `Koleksiyonu Göster`: Tüm oyunları listeler.

**Fotoğraflar:**
Oyun Eklemme:  




![Oyun Ekleme](https://github.com/user-attachments/assets/36ab7c39-c0d5-411d-9722-c572dc0aff31)


















Oyun Silme:






![Oyun Silme](https://github.com/user-attachments/assets/977c58f0-a67d-40bf-8d0d-d4228e36c7af)









![Oyun silme sonrası](https://github.com/user-attachments/assets/2a4afd5c-9e66-45c0-bf2c-5bdf17e6691b)















Puan Ekleme yanlış girilirse:












![Puan kısmına yanlış birşey girilirse](https://github.com/user-attachments/assets/ea5369da-93b6-4f2f-969a-b6685086c7c1)












Koleksiyon Girdileri:










![Koleksiyonu göstere basıldığında](https://github.com/user-attachments/assets/c119a1f1-c3ef-4254-a659-cdbf00e2df4f)













![Koleksiyona göstere basıldığında ama oyun olmadığında](https://github.com/user-attachments/assets/c9028fff-7d78-4529-afad-b332cb1f6f35)











Bilgiler hatalı veya eksik girilirse:














![Bilgiler hatalı veya eksik girildiyse](https://github.com/user-attachments/assets/050b1e07-b40b-47fe-8f5f-9925c4b1ff6d)















| Bileşen           | Açıklama                                                           |
| ----------------- | ------------------------------------------------------------------ |
| `class Oyun`      | Tek bir oyunu temsil eder (ad, tür, platform, puan listesi içerir) |
| `__init__()`      | Oyun adı, türü, platformu tanımlar ve boş puan listesi oluşturur   |
| `değerlendir()`   | Oyuna puan ekler (listeye)                                         |
| `ortalama_puan()` | Girilen puanların ortalamasını hesaplar                            |
| `__str__()`       | Oyunun bilgilerini formatlı şekilde string'e çevirir               |

| Bileşen            | Açıklama                                          |
| ------------------ | ------------------------------------------------- |
| `class Koleksiyon` | Kullanıcının tüm oyunlarını tutar                 |
| `oyun_ekle()`      | Koleksiyona yeni bir oyun ekler                   |
| `oyun_sil()`       | Koleksiyondan istenen oyunu siler                 |
| `listele()`        | Tüm oyunları string olarak liste halinde döndürür |

| Bileşen             | Açıklama                                                           |
| ------------------- | ------------------------------------------------------------------ |
| `class Oyuncu`      | Oyuncuyu temsil eder, bir adet `Koleksiyon` barındırır             |
| `favorilere_ekle()` | Oyunu koleksiyona ekler (zaten varsa tekrar eklemez)               |
| `oyun_oner()`       | Türüne göre oyun önerisi yapar (aynı türe sahip olanları listeler) |

| Bileşen                        | Açıklama                                                              |
| ------------------------------ | --------------------------------------------------------------------- |
| `class OyunArayuz`             | Tkinter tabanlı kullanıcı arayüzünü temsil eder                       |
| `Entry` alanları               | Oyun adı, türü, platformu ve puanı kullanıcıdan almak için kullanılır |
| `Listbox`                      | Eklenen oyunların listelendiği alan (scrollbar destekli)              |
| `Button`'lar                   | Ekleme, silme, gösterme işlevlerini tetikler                          |
| `guncelle_listbox()`           | Liste kutusunu günceller                                              |
| `kullanici_girdisi_ile_ekle()` | Giriş kutularından bilgileri alarak koleksiyona oyun ekler            |
| `koleksiyondan_sil()`          | Seçilen oyunu siler                                                   |
| `koleksiyonu_goster()`         | Tüm oyunları popup olarak gösterir                                    |

**Ekstra:**
- Yatay ve dikey scroll destekli geniş oyun listesi alanı
- Otomatik liste güncelleme

---

### Kullanım Adımları:
1. Oyun bilgilerini yaz (isim, tür, platform, puan).
2. “Oyun Ekle” butonuna tıkla.
3. “Koleksiyonu Göster” ile tüm oyunları görüntüle.
4. “Seçiliyi Sil” ile oyunları listeden çıkar.

---

---
‍💻 Hazırlayan: Ömer Efe Manduz  
