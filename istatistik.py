from functools import reduce, partial


def buyuk_harfli_gezegenler_fonksiyonel(baglantilar):
    """map kullanarak gezegen isimlerini büyütür."""
    return list(map(str.upper, baglantilar.keys()))

def buyuk_harfli_gezegenler_uretec(baglantilar):
    """Liste üreteci (list comprehension) kullanarak gezegen isimlerini büyütür."""
    return [gezegen.upper() for gezegen in baglantilar.keys()]



def cok_baglantili_gezegenler_fonksiyonel(baglantilar):
    """filter ve lambda kullanarak en az 2 bağlantısı olanları süzer."""
    return list(filter(lambda g: len(baglantilar[g]) >= 2, baglantilar.keys()))

def cok_baglantili_gezegenler_uretec(baglantilar):
    """Liste üreteci kullanarak en az 2 bağlantısı olanları süzer."""
    return [g for g in baglantilar.keys() if len(baglantilar[g]) >= 2]



def toplam_baglanti_fonksiyonel(baglantilar):
    """map ile uzunlukları alıp, reduce ile tümünü toplar."""
    
    return reduce(lambda x, y: x + y, map(len, baglantilar.values()), 0)

def toplam_baglanti_uretec(baglantilar):
    """Yerleşik sum() fonksiyonu ile bağlantı sayılarını toplar."""
    return sum(len(hedefler) for hedefler in baglantilar.values())



def yolculuk(hedef, hiz):
    return f"{hedef} gezegenine {hiz} hızıyla gidiliyor."


hizli_yolculuk = partial(yolculuk, hiz=3)







if __name__ == "__main__":
    
    ornek_baglantilar = {
        "dünya": ["sirius", "centauri"],
        "centauri": ["dünya", "orion"],
        "sirius": ["dünya", "orion", "kara_delik"],
        "orion": ["sirius", "centauri"],
        "kara_delik": []
    }
    
    print("--- 1. BÜYÜK HARFLİ LİSTE ---")
    print("Fonksiyonel: ", buyuk_harfli_gezegenler_fonksiyonel(ornek_baglantilar))
    print("Üreteç:      ", buyuk_harfli_gezegenler_uretec(ornek_baglantilar))
    
    print("\n--- 2. EN AZ İKİ BAĞLANTISI OLANLAR ---")
    print("Fonksiyonel: ", cok_baglantili_gezegenler_fonksiyonel(ornek_baglantilar))
    print("Üreteç:      ", cok_baglantili_gezegenler_uretec(ornek_baglantilar))
    
    print("\n--- 3. TOPLAM BAĞLANTI SAYISI ---")
    print("Fonksiyonel: ", toplam_baglanti_fonksiyonel(ornek_baglantilar))
    print("Üreteç:      ", toplam_baglanti_uretec(ornek_baglantilar))
    
    print("\n--- 4. PARTIAL (SABİT HIZ) ---")
    print(hizli_yolculuk(hedef="orion"))  