import google.generativeai as genai
import os
import time
from datetime import datetime

# API key
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

PROMPT = f"""
Bugün {datetime.now().strftime('%d %B %Y')} tarihi için aşağıdaki kategorilerde güncel, önemli haberler topla.

KAYNAKLAR: The Guardian, MIT Technology Review, Nature, Science, Reuters, BBC, AP, NPR, The Atlantic, Wired, NEJM, The Economist, Lancet, New Scientist — yalnızca güvenilir, hakemli veya editoryal standartları yüksek yayınlar.

KATEGORİLER VE FORMAT:
Her kategori için 3 haber yaz. Format TAM OLARAK şöyle olsun:

🌍 DÜNYADAN
• Haber başlığı ve özeti — bağlam veya sonuç. → Kaynak Adı
• Haber başlığı ve özeti — bağlam veya sonuç. → Kaynak Adı
• Haber başlığı ve özeti — bağlam veya sonuç. → Kaynak Adı

⚡ TEKNOLOJİ & YAPAY ZEKA
• Haber başlığı ve özeti — bağlam veya sonuç. → Kaynak Adı
• Haber başlığı ve özeti — bağlam veya sonuç. → Kaynak Adı
• Haber başlığı ve özeti — bağlam veya sonuç. → Kaynak Adı

🔬 BİLİM & SAĞLIK
• Haber başlığı ve özeti — bağlam veya sonuç. → Kaynak Adı
• Haber başlığı ve özeti — bağlam veya sonuç. → Kaynak Adı
• Haber başlığı ve özeti — bağlam veya sonuç. → Kaynak Adı

📚 KÜLTÜR & KİTAP
• Haber başlığı ve özeti — bağlam veya sonuç. → Kaynak Adı
• Haber başlığı ve özeti — bağlam veya sonuç. → Kaynak Adı
• Haber başlığı ve özeti — bağlam veya sonuç. → Kaynak Adı

KURALLAR:
- Türkçe yaz
- Em dash (—) kullan ayraç olarak
- Gerçek, doğrulanabilir haberler seç
- Sensasyonel değil, önemli haberleri seç
- Sadece bu formatı kullan, başka açıklama ekleme
"""

def uret_haberler():
    model = genai.GenerativeModel("gemini-2.0-flash")
    
    # 3 kez dene, her denemede biraz bekle
    for deneme in range(3):
        try:
            print(f"Deneme {deneme + 1}...")
            response = model.generate_content(PROMPT)
            return response.text
        except Exception as e:
            hata = str(e)
            print(f"Hata: {hata}")
            if "429" in hata or "quota" in hata.lower() or "rate" in hata.lower():
                bekleme = 60 * (deneme + 1)  # 60s, 120s, 180s
                print(f"Kota aşıldı, {bekleme} saniye bekleniyor...")
                time.sleep(bekleme)
            else:
                raise e
    
    raise Exception("3 denemede de başarısız oldu.")

def html_olustur(haberler_metni):
    tarih = datetime.now().strftime('%d %B %Y')
    gun = datetime.now().strftime('%A')
    
    # Türkçe gün adları
    gunler = {
        'Monday': 'Pazartesi', 'Tuesday': 'Salı', 'Wednesday': 'Çarşamba',
        'Thursday': 'Perşembe', 'Friday': 'Cuma', 'Saturday': 'Cumartesi', 'Sunday': 'Pazar'
    }
    gun_tr = gunler.get(gun, gun)

    # Haberleri parse et ve HTML'e çevir
    satirlar = haberler_metni.strip().split('\n')
    html_icerik = ""
    
    kategori_ikonlar = {
        '🌍': ('dunya', 'Dünyadan'),
        '⚡': ('teknoloji', 'Teknoloji & Yapay Zeka'),
        '🔬': ('bilim', 'Bilim & Sağlık'),
        '📚': ('kultur', 'Kültür & Kitap')
    }
    
    mevcut_kategori = None
    haberler = []
    
    for satir in satirlar:
        satir = satir.strip()
        if not satir:
            continue
        
        # Kategori başlığı mı?
        kategori_bulundu = False
        for ikon, (cls, ad) in kategori_ikonlar.items():
            if ikon in satir:
                # Önceki kategoriyi kapat
                if mevcut_kategori and haberler:
                    html_icerik += f'<div class="kategori {mevcut_kategori[0]}">'
                    html_icerik += f'<h2>{mevcut_kategori[1]}</h2>'
                    for haber in haberler:
                        html_icerik += f'<div class="haber"><p>{haber}</p></div>'
                    html_icerik += '</div>'
                
                mevcut_kategori = (cls, f'{ikon} {ad}')
                haberler = []
                kategori_bulundu = True
                break
        
        if not kategori_bulundu and satir.startswith('•') and mevcut_kategori:
            haber_metni = satir.lstrip('•').strip()
            haberler.append(haber_metni)
    
    # Son kategoriyi kapat
    if mevcut_kategori and haberler:
        html_icerik += f'<div class="kategori {mevcut_kategori[0]}">'
        html_icerik += f'<h2>{mevcut_kategori[1]}</h2>'
        for haber in haberler:
            html_icerik += f'<div class="haber"><p>{haber}</p></div>'
        html_icerik += '</div>'

    html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Günün Akışı — {tarih}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Georgia', serif;
            background: #f5f0e8;
            color: #1a1a1a;
            min-height: 100vh;
        }}
        header {{
            background: #1a1a1a;
            color: #f5f0e8;
            padding: 2rem;
            text-align: center;
            border-bottom: 4px solid #c8a96e;
        }}
        header h1 {{
            font-size: 2.5rem;
            letter-spacing: 0.1em;
            margin-bottom: 0.3rem;
        }}
        header .tarih {{
            font-size: 0.95rem;
            opacity: 0.7;
            letter-spacing: 0.05em;
            font-style: italic;
        }}
        .container {{
            max-width: 860px;
            margin: 2.5rem auto;
            padding: 0 1.5rem;
        }}
        .kategori {{
            background: white;
            border-radius: 2px;
            margin-bottom: 2rem;
            border-left: 4px solid #c8a96e;
            padding: 1.5rem 2rem;
            box-shadow: 0 1px 4px rgba(0,0,0,0.07);
        }}
        .kategori.dunya {{ border-left-color: #2c5f8a; }}
        .kategori.teknoloji {{ border-left-color: #2d6a4f; }}
        .kategori.bilim {{ border-left-color: #7b2d8b; }}
        .kategori.kultur {{ border-left-color: #c8522a; }}
        .kategori h2 {{
            font-size: 0.8rem;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            color: #666;
            margin-bottom: 1.2rem;
            padding-bottom: 0.7rem;
            border-bottom: 1px solid #eee;
        }}
        .haber {{
            padding: 0.8rem 0;
            border-bottom: 1px solid #f0ece4;
        }}
        .haber:last-child {{ border-bottom: none; }}
        .haber p {{
            font-size: 1rem;
            line-height: 1.65;
            color: #2a2a2a;
        }}
        footer {{
            text-align: center;
            padding: 2rem;
            color: #999;
            font-size: 0.8rem;
            border-top: 1px solid #ddd;
            margin-top: 2rem;
        }}
        @media (max-width: 600px) {{
            header h1 {{ font-size: 1.8rem; }}
            .kategori {{ padding: 1rem 1.2rem; }}
        }}
    </style>
</head>
<body>
    <header>
        <h1>Günün Akışı</h1>
        <div class="tarih">{gun_tr}, {tarih}</div>
    </header>
    <div class="container">
        {html_icerik}
    </div>
    <footer>
        Güvenilir kaynaklardan derlendi · Her gün güncellenir
    </footer>
</body>
</html>"""
    
    return html

# Ana akış
print("Haberler üretiliyor...")
haberler = uret_haberler()
print("Haberler alındı, HTML oluşturuluyor...")

html = html_olustur(haberler)

with open("haberler.html", "w", encoding="utf-8") as f:
    f.write(html)

print("haberler.html oluşturuldu!")
print("\n--- Üretilen haberler ---")
print(haberler)
