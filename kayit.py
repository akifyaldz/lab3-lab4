def gorev_kaydi(baslik, *adimlar, oncelik="normal", **ekler):
    """Görev başlığını, adımlarını ve ek bilgileri formatlayarak bir metin oluşturur."""
    
    sonuc = f"[{oncelik}] {baslik}\n"
    
    numara = 1 
    for adim in adimlar:
        
        sonuc = sonuc + f"  {numara}. {adim}\n"
        numara += 1

    for anahtar, deger in ekler.items():
        sonuc = sonuc + f"{anahtar}: {deger}\n"
        
    return sonuc.strip()

if __name__ == "__main__":
    print("--- 1. Çağrı Biçimi (Standart) ---")
    cikti_1 = gorev_kaydi(
        "Kara deliğe atla", 
        "Kredi kazan", "Pilot bul", "Hiperdrive al", 
        oncelik="YÜKSEK", 
        sorumlu="Ayşe"
    )
    print(cikti_1)
    
    print("\n--- 2. Çağrı Biçimi (Liste ve Sözlük Açarak) ---")
    adimlar_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler_sozlugu = {"sorumlu": "Ayşe"}
    
    cikti_2 = gorev_kaydi(
        "Kara deliğe atla", 
        *adimlar_listesi, 
        oncelik="YÜKSEK", 
        **ekler_sozlugu 
    )
    print(cikti_2)