from uzay_oyunu.tuzaklar import yakit_ekle

def test_yakit_ekle_tuzagi():
    # 1. Çağrı: Sadece 10 birim yakıt ekliyoruz. Beklenen sonuç: [10]
    sonuc1 = yakit_ekle(10)
    assert sonuc1 == [10]
    
    # 2. Çağrı: BAŞKA bir gemi için sadece 20 birim ekliyoruz. 
    # Normalde bunun da temiz bir listeyle sadece [20] dönmesini bekleriz.
    sonuc2 = yakit_ekle(20)
    assert sonuc2 == [20] # AMA BURASI HATA VERECEK!