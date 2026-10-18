import time

def zamanlayici(aralik):
    """Belirtilen aralık (saniye) geçince True, aksi halde False üreten meşgul bekleme üreteci."""
    son_zaman = time.time()
    while True:
        su_an = time.time()
        if su_an - son_zaman >= aralik:
            yield True
            son_zaman = su_an
        else:
            yield False

def bonus_gorev():
    print("10 saniyelik zamanlayıcı başladı (Lütfen fan sesini dinleyin)...\n")
    
    
    tik_ureteci = zamanlayici(2)
    tak_ureteci = zamanlayici(5)
    
    baslangic = time.time()
    
    
    while time.time() - baslangic <= 10:
        
        if next(tik_ureteci):
            print(f"[{time.time() - baslangic:.1f} sn] tik")
            
        if next(tak_ureteci):
            print(f"[{time.time() - baslangic:.1f} sn] tak")

if __name__ == "__main__":
    bonus_gorev()