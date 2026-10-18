from uzay_oyunu.oyun import envanter_metni, hedef_menusu

def test_envanter_bos():
    # Kural: Hiçbir eşya yoksa (False, False, False), sonuç boş bir metin ("") olmalı.
    assert envanter_metni(False, False, False) == ""


def test_envanter_metni_dolu ():
    assert envanter_metni(True,False,True) == "Sende: bol kredi, yetenekli bir pilot"

def test_hedef_menusu():
    beklenen_cikti  = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
    assert hedef_menusu(["centauri","sirius"]) == beklenen_cikti