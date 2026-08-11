from src.cart_processor import sepeti_hesapla

def test_eksik_ve_bozuk_sepet_verisi():
    # Eksik anahtarlar ve eksik ürün detayları içeren bozuk sepet verisi
    bozuk_sepet = {
        "urunler": [
            {"ad": "Laptop"} # 'fiyat' ve 'adet' bilgisi yok! KeyError patlatacak.
        ]
        # 'indirim_kodu' ve 'kullanici_tipi' tamamen eksik!
    }
    
    sonuc = sepeti_hesapla(bozuk_sepet)
    assert sonuc["toplam"] == 0.0