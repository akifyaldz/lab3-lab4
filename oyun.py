from uzay_oyunu.akis import yakit_gostergesi

def travel(galaksi_yakit_degeri=100):
    
    gosterge = yakit_gostergesi(galaksi_yakit_degeri, 5)
    
    
    while True:
        
        try:
           
            kalan_yakit = next(gosterge)
            print(f"Yolculuk başarılı! Kalan yakıtın: {kalan_yakit}")
            
        except StopIteration:
            
            print("Yakıtın bitti, uzayda sürükleniyorsun...")
            break 
def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Oyuncunun elindeki eşyaları bir metin olarak birleştirip döndürür."""
    
    
    if credits == False and engines == False and copilot == False:
        return ""


    esyalar = []
    if credits ==True:
        esyalar.append("bol kredi")
    if engines == True:
        esyalar.append("motor parcasi")
    if copilot == True:
        esyalar.append("yetenekli bir pilot")

    esyalar = ", ".join(esyalar)
    return "Sende: " + esyalar


hedefler = ["centauri", "sirius"]
def hedef_menusu(hedefler: list[str]) -> str:
    """Verilen hedefleri numaralandırarak bir menü metni oluşturur."""
    
    
    menu_metni = "Nereye gitmek istersin?\n"

    numara = 1
    for hedef in hedefler : 
        menu_metni = menu_metni + f"[{numara}] {hedef}\n"

        numara +=1

    return menu_metni.strip()
    