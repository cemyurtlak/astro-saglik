# Geliştirme Günlüğü – Astro Sağlık

(En yeni aşama en üstte)

---

## Aşama 4 – GitHub'a yükleme ve internetten oynanabilir link
**Tarih:** 2026-11-10

**İstek:** Projeyi GitHub'a yükle; link gönderildiğinde başka bilgisayarlarda da çalışsın.

**Yapılanlar:**
- GitHub'da herkese açık depo oluşturuldu: https://github.com/cemyurtlak/astro-saglik
- Tüm proje dosyaları yüklendi (oyun, `lib/three.min.js`, tek dosya sürüm, görseller, sunumlar, kayıt dosyaları).
- **GitHub Pages** açıldı (main dalı, kök klasör) → oyun linki: https://cemyurtlak.github.io/astro-saglik/
- README'ye oynama ve kaynak kod linkleri eklendi.

**Değişen dosyalar:** `README.md`, `GELISTIRME_GUNLUGU.md`, `DEVAM_NOTLARI.md` (oyun kodu değişmedi)

**Test durumu:** Depo içeriği GitHub API ile kontrol edildi (16 kayıt, dosya boyutları yerel dosyalarla aynı). Pages linki yayına alındıktan sonra açılıp test edildi.

---

## Aşama 3 – Yarışma sunumları (Demo + Tam)
**Tarih:** 2026-11-10

**İstek:** `sunum` klasörüne iki sunum: Demo Sunum ve Tam Sunum; NASA Space Apps Challenge kurallarına uygun olsun.

**Uygulanan Space Apps kuralları (Project Submission Guide):**
- Demo slayt sunumu **en fazla 7 slayt (kapak dahil)** → Demo tam 7 slayt.
- Sunum dili **İngilizce** (bağlantılı tüm materyaller İngilizce olmalı) → slaytlar İngilizce, konuşmacı notları İngilizce + Türkçe.
- Slaytlarda **takım adı, üye adı ve seçilen challenge** → kapakta yazıyor (AstroPulse · Azra Kurt · Create Health Monitoring Software…).
- Projeyi, kullanıcı deneyimini ve **NASA verisi/biliminin** nasıl kullanıldığını gösteren görseller → oyun ekran görüntüleri + "Built on NASA science" slaytı.
- **Yapay zekâ kullanımı açıkça belirtildi**; yapay zekâ ile üretilmiş görsellere (logo, takım görseli) görünür **"AI-generated image" filigranı** eklendi.
- **NASA logosu / amblemi kullanılmadı.** Gerçek çocuk fotoğrafı yok (takım görseli çizim).
- Tam sunumda kaynaklar (NASA kaynakları + araçlar/lisanslar) listelendi; jüri kriterlerine (Etki, Yaratıcılık, Geçerlilik, Uygunluk, Sunum) göre akış kuruldu.

**Yapılanlar:**
- Oyundan Playwright ile ekran görüntüleri alındı (menü, oyun, alarm, tarama, karar sorusu, güneş patlaması, sağlık karnesi).
- `sunum/AstroPulse_Demo_Sunum.pptx` (7 slayt) ve `sunum/AstroPulse_Tam_Sunum.pptx` (16 slayt) + ikisinin PDF'i.
- Tasarım: lacivert uzay teması, logo renkleri (cyan, kırmızı, sarı), yuvarlak kartlar ve renkli ikon daireleri.

**Değişen/oluşan dosyalar:** `sunum/AstroPulse_Demo_Sunum.pptx`, `sunum/AstroPulse_Demo_Sunum.pdf`, `sunum/AstroPulse_Tam_Sunum.pptx`,
`sunum/AstroPulse_Tam_Sunum.pdf`, `README.md`, `GELISTIRME_GUNLUGU.md`, `DEVAM_NOTLARI.md` (oyun kodu değişmedi)

**Test durumu:** İki sunum da PowerPoint dosya doğrulamasından geçti; her slayt görüntüye çevrilip kontrol edildi (taşma/çakışma düzeltildi).

---

## Aşama 2 – Fareyle bakış + oyuncunun gözünden kamera
**Tarih:** 2026-10-16

**İstek:** Fare hareket ettirildiğinde bakış açısı (kamera) otomatik dönsün; oyuncunun gözünden (1. şahıs) bakma seçeneği olsun.

**Yapılanlar:**
- **Fare kilidi (Pointer Lock):** Bilgisayarda BAŞLA'ya basınca fare kilitlenir; artık tuşa basılı tutmadan fareyi oynatmak kamerayı döndürür.
  Modal/duraklatma/ekranlarda kilit otomatik bırakılır; modal kapanınca veya "devam" deyince yeniden kilitlenir.
  Kilit yoksa ekranda "Fareyle etrafa bakmak için ekrana tıkla" ipucu çıkar. `Esc` fareyi serbest bırakır.
- **Göz kamerası (1. şahıs):** `V` tuşu veya üst çubuktaki 👁/🎥 butonu ile geçiş. Kamera kafa hizasında, yürürken hafif sallanma,
  ekranın ortasında nişangâh noktası, karakter gizlenir ve hep bakılan yöne döner. Tercih `localStorage`'da saklanır.
- **Tekerlek:** En yakına kadar yakınlaşınca göz kamerasına geçer; gözdeyken tekerleği geri çevirince arkadan kameraya döner (Roblox gibi).
- Tablette sürükleyerek bakış aynen çalışır; 👁 butonu tablette de var.
- Nasıl Oynanır ve alt ipucu metinleri güncellendi.

**Değişen dosyalar:** `index.html`, `AstroSaglik_TekDosya.html`, `README.md`, `GELISTIRME_GUNLUGU.md`, `DEVAM_NOTLARI.md`

**Test durumu:** Playwright (Chromium, 1366×768): oyun başlayınca fare kilitlendi, gerçek fare hareketi kamerayı döndürdü,
`V` ile göz kamerası açıldı (karakter bakış yönüne döndü, yürüme çalıştı), tekerlekle arkadan kameraya dönüldü,
kilit bırakılınca ipucu göründü, 👁 butonu çalıştı. JavaScript hatası yok (yalnızca Google yazı tipi internet olmadığı için yüklenmedi).

---

## Aşama 1 – İlk sürüm: 3B sağlık izleme oyunu
**Tarih:** 2026-10-08

**İstek:** NASA Space Apps Challenge 2026 "Create Health Monitoring Software for Astronauts on Space Missions"
için, tablet dahil her ortamda çalışan, görsel olarak güzel, Roblox benzeri bir web oyunu. Oyun sonunda skor olsun,
kişiler sırayla oynayabilsin ve her kişinin oyun sonunda puanı yazsın. Klasör: `6NEWTONAzraKurt`.

**Yapılanlar:**
- Three.js (r149) ile 3B uzay istasyonu: platform, 7 istasyon binası, merkez hologram, güneş panelleri, Dünya, Ay, yıldızlar.
- Roblox tarzı blok astronot karakteri (yürüme/zıplama animasyonu, isim etiketi, seçilebilir renk).
- 3. şahıs kamera (sürükle/yakınlaş), kamera bina içine girmesin diye çarpışma kontrolü.
- 7 sağlık göstergesi, zamanla azalma (günler ilerledikçe hızlanır), kritik uyarılar, kırmızı kenar efekti.
- Mini oyunlar: sağlık taraması + değerlendirme, egzersiz (koşu bandı / ARED), dengeli öğün seçimi, uyku hazırlığı,
  sera sulama, duygu kontrolü + aile görüşmesi, radyasyon sığınağı sorusu + koruyucu yelek.
- Sağlık olayları (7 tür + güneş patlaması), hedef ışını, yön oku, mini harita.
- Günlük görevler, kristaller, parkur kutuları.
- Menü: oyuncu ekleme (en fazla 8, renk seçimi), görev süresi (3/5/7 gün), nasıl oynanır, rekorlar.
- Sıra ekranı → oyun → Sağlık Karnesi (puan, yıldız, istatistik, gösterge çubukları, günlük grafik, ruh hali günlüğü, ipucu) → sonraki oyuncu → podyum ve sıralama.
- Dokunmatik kontroller (joystick, KULLAN, ZIPLA), tam ekran, ses (WebAudio).
- Tek dosya sürüm üreten `tek_dosya_olustur.py`.

**Değişen/oluşan dosyalar:** `index.html`, `lib/three.min.js`, `AstroSaglik_TekDosya.html`, `tek_dosya_olustur.py`,
`README.md`, `GELISTIRME_GUNLUGU.md`, `DEVAM_NOTLARI.md`

**Test durumu:** Playwright (Chromium) ile 1366×768 masaüstü ve 1024×768 dokunmatik tablet görünümünde test edildi:
menü, oyuncu ekleme, sıra ekranı, hareket, olay tetikleme, tarama + soru, tüm istasyon modalları, spor dokunma oyunu,
sera oyunu, güneş patlaması, gün geçişi, tıbbi tahliye, karne ve sonuç ekranı. JavaScript hatası yok
(test ortamında sadece Google yazı tipi internet olmadığı için yüklenmedi; yedek yazı tipi devreye giriyor).
