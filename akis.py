from typing import Generator
from functools import lru_cache
from typing import Dict, List, Callable

def fibonacci() -> Generator[int, None, None]:
    """
    Sonsuz bir Fibonacci dizisi üreten üreteç (generator) fonksiyonu.
    Her çağrıldığında dizinin bir sonraki elemanını döndürür.
    İlk iki değer 0 ve 1'dir. Sonraki değerler önceki ikisinin toplamıdır.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def yakit_gostergesi(yakit: int, tuketim: int) -> Generator[int, None, None]:
    """
    Başlangıç yakıtını her çağrıldığında tüketim miktarı kadar azaltan üreteç.
    Yakıt sıfırın altına düşerse 0 döndürür ve durur (StopIteration fırlatır).
    """
    while yakit > 0:
        yakit -= tuketim
        if yakit < 0:
            yakit = 0
        yield yakit



from typing import Iterable, Tuple

def satirlari_oku(yol: str) -> Generator[str, None, None]:
    """Dosyayı satır satır okur, boş ve '#' ile başlayan satırları atlar."""
    with open(yol, 'r', encoding='utf-8') as f:
        for satir in f:
            temiz_satir = satir.strip()
            
            if temiz_satir and not temiz_satir.startswith('#'):
                yield temiz_satir

def ayristir(satirlar: Iterable[str]) -> Generator[Tuple[str, str, int], None, None]:
    """'kaynak -> hedef yakit' formatındaki satırları ayrıştırıp demet üretir."""
    for satir in satirlar:
        kisimlar = satir.split()
        
        if len(kisimlar) == 4 and kisimlar[1] == '->':
            kaynak = kisimlar[0]
            hedef = kisimlar[2]
            yakit = int(kisimlar[3])
            yield (kaynak, hedef, yakit)

def uzun_yolculuklar(kayitlar: Iterable[Tuple[str, str, int]], esik: int) -> Generator[Tuple[str, str, int], None, None]:
    """Yakıt tüketimi belirtilen eşik değerinden büyük olan kayıtları süzer."""
    for kayit in kayitlar:
        
        if kayit[2] > esik:
            yield kayit





def rota_sayaci(baglantilar: Dict[str, List[str]]) -> Callable[[str, int], int]:
    """
    Belirli bir gezegenden başlayıp tam 'adim' sayısı kadar yolculuk 
    yapan farklı rotaların sayısını hesaplayan önbellekli (cache) bir fonksiyon döndürür.
    """
    
    
    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
        
        if adim == 0:
            return 1
            
        
        if gezegen not in baglantilar or not baglantilar[gezegen]:
            return 0
            
        
        toplam_rota = 0
        for komsu in baglantilar[gezegen]:
            toplam_rota += rota_sayisi(komsu, adim - 1)
            
        return toplam_rota

    return rota_sayisi