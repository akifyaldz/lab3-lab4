def hamle_sayaci():
    """Her çağrıldığında sayacı bir artıran bir fonksiyon (closure) döndürür."""
    sayac = 0
    
    def artir():
        nonlocal sayac 
        sayac += 1
        return sayac
        
    return artir

def en_bagli_gezegenler(galaksi):
    """
    Gezegenleri bağlantı sayısına göre azalan, 
    eşitlik durumunda alfabetik sırayla artan şekilde sıralar.
    galaksi parametresinin { 'gezegen': ['baglanti1', 'baglanti2'] } yapısında bir sözlük olduğu varsayılmıştır.
    """
    
    sirali_liste = sorted(galaksi.keys(), key=lambda gezegen: (-len(galaksi[gezegen]), gezegen))
    return sirali_liste


if __name__ == "__main__":
    
    say = hamle_sayaci()
    say()  
    say() 
    toplam = say() 
    print(f"Oyunu {toplam} hamlede bitirdin!")
    
    
    g = {
        'sirius': ['1', '2', '3', '4'],
        'centauri': ['1', '2', '3'],
        'dünya': ['1', '2'],
        'orion': ['1'],
        'kara_delik': []
    }
    
    print(">>> en_bagli_gezegenler(g)")
    print(en_bagli_gezegenler(g))