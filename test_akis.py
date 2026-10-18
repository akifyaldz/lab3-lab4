from itertools import islice, takewhile
from uzay_oyunu.akis import fibonacci

def test_fibonacci_olusturma():
    """next() kullanarak ilk üç değeri (0, 1, 1) alır ve test eder."""
    g = fibonacci()
    assert next(g) == 0
    assert next(g) == 1
    assert next(g) == 1

def test_fibonacci_araclar():
    """islice ve takewhile kullanarak belirli kesitleri test eder."""
    # islice ile ilk 12 değer
    ilk_12 = list(islice(fibonacci(), 12))
    assert ilk_12 == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    
    # takewhile ile 100'den küçük değerler
    yuzden_kucukler = list(takewhile(lambda x: x < 100, fibonacci()))
    assert yuzden_kucukler == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def test_fibonacci_tek_kullanimlik():
    """
    Üretecin tek kullanımlık olduğunu test eder. 
    Aynı üreteç üzerinden islice çağrıldığında baştan başlamaz, kaldığı yerden devam eder.
    """
    g = fibonacci()
    
    # Aynı 'g' üretecinden ilk 5 değeri çekelim: [0, 1, 1, 2, 3]
    ilk_cekis = list(islice(g, 5))
    assert ilk_cekis == [0, 1, 1, 2, 3]
    
    # Aynı 'g' üretecinden bir sonraki 5 değeri çekelim (Kaldığı yerden devam etmeli)
    ikinci_cekis = list(islice(g, 5))
    assert ikinci_cekis == [5, 8, 13, 21, 34]
    
    # İki sonucun birbirinden farklı olduğunu kanıtlayalım (Tek kullanımlık kuralı)
    assert ilk_cekis != ikinci_cekis


from uzay_oyunu.akis import yakit_gostergesi

def test_yakit_gostergesi():
    """Yakıt göstergesinin doğru adımlarla azaldığını ve 0'da durduğunu test eder."""
    gosterge = yakit_gostergesi(100, 30)
    beklenen_sonuc = [70, 40, 10, 0]
    
    assert list(gosterge) == beklenen_sonuc


from uzay_oyunu.akis import satirlari_oku, ayristir, uzun_yolculuklar

def test_seyir_defteri_boru_hatti():
    """Veri boru hattının doğru ayrıştırıp süzdüğünü test eder."""
    yol = "veri/seyir.txt"
    
    # 1. Test: Toplam yakıtın 88 olması
    toplam_yakit = sum(y for _, _, y in ayristir(satirlari_oku(yol)))
    assert toplam_yakit == 88
    
    # 2. Test: Eşik değeri 10'dan büyük olan uzun yolculukların hedefleri
    kayitlar = ayristir(satirlari_oku(yol))
    uzun_hedefler = [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)]
    assert uzun_hedefler == ['sirius', 'centauri', 'orion', 'kara_delik']


from uzay_oyunu.akis import rota_sayaci

def test_onbellekli_rota_sayaci():
    """Önbellekli rota sayacının matematiğini izole bir mini galaksiyle test eder."""
    # Test için sahte, kontrollü bir bağlantı ağı kuruyoruz
    ornek_baglantilar = {
        "dünya": ["sirius", "centauri"],
        "sirius": ["orion", "kara_delik"],
        "centauri": ["dünya"],
        "orion": ["dünya"],
        "kara_delik": []
    }
    
    say = rota_sayaci(ornek_baglantilar)
    
    # 0 adım varsa sadece olduğu yerde durur (1 rota)
    assert say("dünya", 0) == 1
    
    # kara_delik'ten çıkış yok, adım atılamaz (0 rota)
    assert say("kara_delik", 5) == 0
    
    # dünya'dan 1 adımda gidilecek yerler: sirius ve centauri (2 rota)
    assert say("dünya", 1) == 2
    
    # dünya'dan 2 adımda gidilecek yerler:
    # 1. dünya -> sirius -> orion
    # 2. dünya -> sirius -> kara_delik
    # 3. dünya -> centauri -> dünya
    # Toplam: 3 rota
    assert say("dünya", 2) == 3