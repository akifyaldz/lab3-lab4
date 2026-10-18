import json


def galaksi_kur(gezegenler, baglantilar, baslangic, **kwargs):
    """JSON dosyasından gelen verilerle oyun haritasını kurar ve denetler."""
    
    
    if baslangic not in gezegenler:
        raise ValueError("Başlangıç gezegeni listede bulunamadı!")
        
    
    yakit = kwargs.get("yakit", 50)
    
    
    print("--- Galaksi Başarıyla Kuruldu ---")
    print(f"Gezegenler: {gezegenler}")
    print(f"Başlangıç Noktası: {baslangic}")
    print(f"Başlangıç Yakıtı: {yakit}")
    
    return yakit


import os

if __name__ == "__main__":
    
    bulundugumuz_klasor = os.path.dirname(__file__)
    dosya_yolu = os.path.join(bulundugumuz_klasor, "galaksi.json")
    
    
    with open(dosya_yolu, "r", encoding="utf-8") as dosya:
        veri = json.load(dosya)
        
    
    galaksi_kur(**veri)