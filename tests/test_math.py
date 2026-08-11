from src.math_operations import hesapla_ortalama

def test_bos_liste_hatasi():
    # Boş liste gönderiyoruz, fonksiyon patlayacak
    sonuc = hesapla_ortalama([])
    assert sonuc == 0