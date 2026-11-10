# 🚀 Astro Sağlık – Uzay İstasyonu Sağlık Görevi

**NASA Space Apps Challenge 2026** – *Create Health Monitoring Software for Astronauts on Space Missions*
(Uzay Görevlerindeki Astronotlar İçin Sağlık İzleme Yazılımı Oluşturma) yarışması için hazırlanan 3B web oyunu.

## Amaç
Uzun süreli görevlerde astronotlar radyasyon, izolasyon, kapalı alan ve değişen yerçekimi nedeniyle
bağışıklık değişiklikleri, kemik kaybı, kalp-damar sorunları ve davranışsal sağlık sorunları yaşayabilir.
Bu oyunda oyuncu bir astronotu kontrol eder ve sağlığını kendisi izler:

1. **Veri topla** – Tıp Merkezinde sağlık taraması (nabız, tansiyon, SpO₂, vücut ısısı, kemik yoğunluğu, radyasyon dozu, stres, uyku, vücut suyu).
2. **Değerlendir** – Verilere bakıp en riskli alanı / doğru kararı seç.
3. **Harekete geç** – İlgili istasyona gidip egzersiz, beslenme, uyku, bitki bakımı, aile görüşmesi veya radyasyon korunması yap.

## Özellikler
- Roblox tarzı blok karakterli 3B uzay istasyonu (Three.js), Dünya ve Ay manzarası
- 7 sağlık göstergesi: Kalp-Damar, Kemik & Kas, Bağışıklık, Radyasyon Güvenliği, Ruh Hali, Uyku & Enerji, Su & Beslenme
- 7 istasyon ve mini oyunlar: 🩺 Tıp Merkezi, 🏋️ Spor Alanı, 🍽️ Mutfak, 🌱 Sera, 📡 İletişim Odası, 🛏️ Uyku Kabini, ☢️ Radyasyon Sığınağı
- Rastgele sağlık olayları (ateş, çarpıntı, bulanık görme/SANS, stres, kemik ağrısı, susuzluk, uykusuzluk) ve ☀️ güneş patlaması
- Günlük görevler, veri kristalleri, parkur kutuları ve altın kristal
- **Sırayla çok oyunculu**: oyuncular eklenir, herkes sırayla oynar, her oyuncunun sonunda **Sağlık Karnesi ve puanı** gösterilir, en sonda **podyum + sıralama**
- Tüm zamanların rekor tablosu (tarayıcıda saklanır)
- **Fareyle serbest bakış** ve **oyuncunun gözünden (1. şahıs) kamera** seçeneği
- Bilgisayar (klavye + fare) ve **tablet/telefon** (joystick + dokunmatik butonlar) desteği, tam ekran
- Gerçek NASA bilgileriyle "Gerçek uzayda" bilgi kutuları

## Takım ve Sunumlar
- **Takım adı:** AstroPulse · **Üye:** Azra Kurt (tek kişilik takım)
- `sunum/` klasöründe iki sunum var. **Demo Sunum**, Space Apps'in "Project Demo" kuralına göre en fazla 7 slayt ve İngilizcedir;
  Google Drive / OneDrive'a yüklenip **herkese açık link** olarak proje sayfasına eklenir (siteye dosya yüklenemez).
- **Tam Sunum** 16 slayttır; konuşmacı notları İngilizce + Türkçedir.

## Kurulum / Çalıştırma
Kurulum gerekmez.
- **🌐 İnternetten oyna (her bilgisayar/tablet):** https://cemyurtlak.github.io/astro-saglik/
- **Kaynak kod (GitHub):** https://github.com/cemyurtlak/astro-saglik
- **Bilgisayarda:** `index.html` dosyasına çift tıkla (Chrome / Edge önerilir). `lib/three.min.js` dosyası yanında olmalı.
- **Tablette (internetsiz):** `AstroSaglik_TekDosya.html` dosyasını tablete kopyala ve tarayıcıda aç (tek dosya, her şey içinde).
- **Paylaşım linki:** Oyun ayrıca Claude Artifact olarak yayınlandı; link ile her cihazdan açılabilir.

`index.html` değiştirildikten sonra tek dosya sürümünü yenilemek için:
```
python tek_dosya_olustur.py
```

## Kontroller
| Bilgisayar | Tablet |
|---|---|
| W A S D / Ok tuşları: yürü | Sol alttaki joystick |
| Boşluk: zıpla | ZIPLA butonu |
| E / Enter: istasyonu kullan | KULLAN butonu veya alttaki yazıya dokun |
| Fareyi oynat: etrafa bak (oyun başlayınca fare kilitlenir; kilit yoksa ekrana bir kez tıkla) | Ekranı sürükle: kamera |
| V veya 👁 butonu: oyuncunun gözünden / arkadan kamera | 👁 butonu |
| Tekerlek: yakınlaş (en yakında göz kamerasına geçer) | – |
| Esc: fareyi serbest bırak (butonlara tıklamak için) | – |
| P / Esc: duraklat | ⏸ butonu |

## Puanlama
| Eylem | Puan |
|---|---|
| Veri kristali / altın kristal | +10 / +30 |
| Günlük sağlık taraması | +60 |
| Doğru değerlendirme (tarama sonrası) | +80 |
| Sağlık olayını doğru çözmek | +150 (yanlış: −20, kaçırmak: −50) |
| Güneş patlamasında sığınağa ulaşmak | +150 |
| Mini oyunlar | +5 … +80 |
| 4 günlük görevin hepsi | +100 |
| Gün sonu sağlık bonusu | ortalama sağlık × 1,5 |
| Görevi tamamlama | 200 + ortalama sağlık × 3 |

Bir gösterge **0** olursa "Tıbbi Tahliye" olur, görev biter (puan kaydedilir).

## Dosya Yapısı
```
6NEWTONAzraKurt/
├── index.html                 # Oyunun tamamı (HTML + CSS + JS)
├── lib/three.min.js           # Three.js r149 (3B grafik kütüphanesi, internetsiz çalışma için)
├── AstroSaglik_TekDosya.html  # Tek dosya sürüm (tablete kopyalamak için)
├── tek_dosya_olustur.py       # Tek dosya sürümünü üreten betik
├── gorseller/                 # Takım logosu ve takım görseli (yapay zekâ ile üretildi)
├── sunum/
│   ├── AstroPulse_Demo_Sunum.pptx / .pdf   # Space Apps "Project Demo" (7 slayt, İngilizce)
│   └── AstroPulse_Tam_Sunum.pptx / .pdf    # Jüri/yerel etkinlik için tam sunum (16 slayt, notlu)
├── README.md
├── GELISTIRME_GUNLUGU.md
└── DEVAM_NOTLARI.md
```
