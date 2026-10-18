import time
import json
from uzay_oyunu.akis import rota_sayaci

with open("uzay_oyunu/galaksi.json", "r", encoding="utf-8") as f:
    galaksi = json.load(f)
baglantilar = galaksi["baglantilar"]

ornek_gezegen = list(baglantilar.keys())[0]

def cachesiz_rota_sayisi(gezegen, adim):
    if adim == 0: return 1
    if gezegen not in baglantilar or not baglantilar[gezegen]: return 0
    return sum(cachesiz_rota_sayisi(k, adim - 1) for k in baglantilar[gezegen])

print(f"--- HIZ KARŞILAŞTIRMASI BAŞLIYOR ({ornek_gezegen.upper()} İÇİN, ADIM=20) ---\n")


basla = time.perf_counter()
sonuc1 = cachesiz_rota_sayisi(ornek_gezegen, 20)
bitis = time.perf_counter()
print(f"Önbellek YOK  -> Sonuç: {sonuc1} | Süre: {bitis - basla:.5f} saniye")


say = rota_sayaci(baglantilar)
basla = time.perf_counter()
sonuc2 = say(ornek_gezegen, 20)
bitis = time.perf_counter()
print(f"Önbellek VAR  -> Sonuç: {sonuc2} | Süre: {bitis - basla:.5f} saniye")

print("\n--- CACHE INFO ---")
print(say.cache_info())