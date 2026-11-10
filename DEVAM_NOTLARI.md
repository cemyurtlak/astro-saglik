# Devam Notları – Astro Sağlık

## Çalışma Kuralları
- Her değişiklikten sonra `GELISTIRME_GUNLUGU.md`'ye yeni aşama ekle (son aşama: **Aşama 4**).
- Özellik/kullanım/dosya yapısı değişirse `README.md`'yi güncelle.
- `index.html` değişince `python tek_dosya_olustur.py` ile `AstroSaglik_TekDosya.html`'i yeniden üret.
- Oyun dili Türkçe; hedef kitle ortaokul öğrencileri → metinler kısa, anlaşılır, eğitici.
- NASA logosu/markası kullanılmaz; sadece yarışma adı metin olarak geçer.

## Teknik Kararlar ve Nedenleri
- **Tek HTML + Three.js r149 (UMD `three.min.js`)**: Derleme aracı gerekmez, `file://` ile çift tıklayınca çalışır
  (ES modülleri `file://`'da CORS hatası verir). r160 sonrası UMD dosyası kaldırıldığı için r149 seçildi.
- **Yerel `lib/` kopyası**: İnternetsiz okul/yarışma ortamında da çalışsın diye CDN yerine.
- **Tek dosya sürüm**: Tablete tek dosya kopyalamak kolay.
- **Fizik**: Basit; döndürülmüş kutu (OBB) çarpışma + kutuların üstüne basma. Kütüphane gerekmez.
- **Zaman**: Modal açıkken oyun duraklar (çocuklar için adil). `dt` en fazla 0,1 sn (yavaş tablette oyun ağırlaşır ama ışınlanma olmaz).
- **Kayıt**: Rekorlar ve oyuncu listesi `localStorage`'da (try/catch ile; açılmazsa oyun yine çalışır).
- **Fareyle bakış = Pointer Lock**: Tarayıcı, fareyi kilitlemek için kullanıcı tıklaması ister; bu yüzden BAŞLA / modal "Devam" /
  duraklatma "devam" tıklamalarında `kilitle()` çağrılır. Oyun dışı durumlarda (`G.durum!=='oyun'`) kamera döngüsü kilidi bırakır.
  Kilitliyken HUD butonlarına tıklanamaz (normal) → `Esc` ile fare serbest kalır, ekrana tıklayınca tekrar kilitlenir.
- **Göz kamerası**: `kam.fp` (açık/kapalı), `kam.bak` (yukarı-aşağı bakış, 3. şahıstaki `kam.pitch`'ten ayrı). Göz modunda
  `avatar.visible=false` (kamera kafanın içinde kalmasın) ve `P.yon=kam.yaw+π` (karakter bakılan yöne döner).
- **Ses**: Dosya yok, WebAudio ile üretilen bip sesleri.

## Kod Haritası (`index.html` içindeki JS)
| Bölüm | Ne yapar |
|---|---|
| Yardımcılar, `Store`, `Ses` | Kısa fonksiyonlar, localStorage, ses efektleri |
| `IND` | 7 sağlık göstergesi (ad, renk, azalma hızı, ilgili istasyon, ipucu) |
| `ISTASYON` | 7 modül (konumlar daire üzerinde otomatik hesaplanır) |
| `OLAYLAR` | Sağlık olayları: mesaj, hedef istasyon, süre, etki, soru-seçenek, bilgi, ödül |
| Three.js sahne | Işık, yıldız, Dünya/Ay, platform, binalar, hologram, paneller, kutular, kristaller |
| `COL`, `cozCarpisma`, `zeminY` | Çarpışma ve zemin yüksekliği |
| `avatarYap`, `hareket`, `avatarAnim` | Blok karakter, hareket, animasyon |
| Girdi | Klavye, `bakisDondur`, fare kilidi (`kilitle/kilitAc`), sürükleme, tekerlek, `kameraModu` (göz/arkadan), joystick, butonlar |
| `yeniGorev`, `guncelle`, `gunSonu` | Görev durumu, zaman, azalma, gün geçişi |
| `olayBaslat/Guncelle/Bitir`, `planOlustur` | Olay zamanlaması (gün 2-4-6'da güneş patlaması) |
| `oyunTip/Spor/Mutfak/Uyku/Sera/Iletisim/Siginak` | Mini oyunlar (modal) |
| `menu`, `nasil`, `rekorlar`, `siraEkrani`, `bitir`, `sonuclar` | Ekranlar ve sıra/puan akışı |
| `kameraGuncelle` | Göz kamerası (kafa hizası) / arkadan kamera (bina çarpışmalı) / menü kamerası |
| `hudGuncelle`, `haritaCiz` | HUD ve mini harita |
| `window.__astro` | Test için dışarı açılmış nesneler |

## GitHub / Yayın
- Depo: https://github.com/cemyurtlak/astro-saglik (herkese açık). Oyun linki: https://cemyurtlak.github.io/astro-saglik/
- GitHub Pages `main` dalının kökünden yayınlanır; `index.html` kökte olmalı, `lib/three.min.js` yolu değişmemeli.
- Güncelleme: değişen dosyaları GitHub'da aynı klasöre "Add file → Upload files" ile yükle; Pages 1-2 dakikada yenilenir.
- Space Apps "Link to Final Project" için oyun linki kullanılabilir (şifresiz, herkese açık).

## Sunum Kuralları (Space Apps)
- Demo: en fazla 7 slayt (kapak dahil) veya en fazla 30 sn video (İngilizce altyazılı). Aşılırsa Global Judging'e giremez.
- Tüm gönderim içeriği İngilizce; slaytlarda takım adı, üye adları ve challenge adı olmalı.
- Yapay zekâ ile üretilmiş görsel/videoda görünür "AI-generated" filigranı şart; yapay zekâ kullanımı açıklanmalı.
- NASA logosu, bayrağı veya görev amblemi kullanılmaz; 18 yaş altının tanınabilir fotoğrafı konmaz.
- Sunumlar pptxgenjs ile üretildi (oluşturma betikleri bu klasörde değil). Değişiklik gerekirse PowerPoint'te düzenlenebilir.
- Oyun arayüzü Türkçe olduğu için slaytlarda "Game UI shown in Turkish" notu var; İngilizce sürüm "Next steps"te.

## Bilinen Sorunlar / Sınırlar
- Fare kilidi bazı gömülü sayfalarda (ör. izin verilmeyen iframe) çalışmayabilir; o zaman sürükleyerek bakış devam eder.
- Kilitliyken `Esc` hem kilidi bırakır hem (tarayıcıya göre) oyunu duraklatabilir.
- Google Fonts (Fredoka) internet yoksa yüklenmez; sistem yazı tipi kullanılır (sorun değil).
- iPhone Safari tam ekran API'sini desteklemez; buton gizlenir.
- Çok eski tabletlerde (WebGL yok) oyun açılmaz, uyarı mesajı gösterilir.

## Sonraki Adım Fikirleri
- Sunumdaki "NASA resources" için proje sayfasına tam linkleri eklemek (şimdilik sadece HRP linki yazılı).
- İngilizce dil seçeneği (NASA jürisi için) – TR/EN sözlük.
- Yarışma sunumu için kısa tanıtım videosu / ekran kaydı.
- Zorluk seviyesi seçimi (azalma hızları).
- Gerçek sensör verisi girişi (ör. akıllı saat nabzı) – "gerçek sağlık takibi" modu.
- Görev sonunda sağlık raporunu PDF/resim olarak indirme.
