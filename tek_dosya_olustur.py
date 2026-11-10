# -*- coding: utf-8 -*-
"""index.html + lib/three.min.js dosyalarını tek bir HTML dosyasında birleştirir.
Çıktı: AstroSaglik_TekDosya.html  (internetsiz tablete kopyalamak için)
Kullanım:  python tek_dosya_olustur.py
"""
from pathlib import Path

kok = Path(__file__).resolve().parent
html = (kok / "index.html").read_text(encoding="utf-8")
three = (kok / "lib" / "three.min.js").read_text(encoding="utf-8")
etiket = '<script src="lib/three.min.js"></script>'
if etiket not in html:
    raise SystemExit("HATA: index.html içinde three.min.js etiketi bulunamadı.")
cikti = html.replace(etiket, "<script>\n" + three + "\n</script>")
(kok / "AstroSaglik_TekDosya.html").write_text(cikti, encoding="utf-8")
print("Tamam -> AstroSaglik_TekDosya.html (%d KB)" % (len(cikti.encode("utf-8")) // 1024))
