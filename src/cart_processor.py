def sepeti_hesapla(sepet_verisi: dict) -> dict:
    if not isinstance(sepet_verisi, dict):
        sepet_verisi = {}

    urunler = sepet_verisi.get("urunler", [])
    if not isinstance(urunler, list):
        urunler = []
    
    ara_toplam = 0.0
    for urun in urunler:
        if isinstance(urun, dict):
            try:
                fiyat = float(urun.get("fiyat", 0))
                adet = int(urun.get("adet", 0))
                if fiyat > 0 and adet > 0:
                    ara_toplam += fiyat * adet
            except (ValueError, TypeError):
                continue
        
    indirim_kodu = sepet_verisi.get("indirim_kodu", "")
    indirim_orani = 0.0
    
    if indirim_kodu == "SUPER20":
        indirim_orani = 0.20
    elif indirim_kodu == "MEGA50":
        indirim_orani = 0.50
        
    indirimli_tutar = ara_toplam * (1 - indirim_orani)
    
    if ara_toplam == 0:
        kargo_ucreti = 0.0
    else:
        kargo_ucreti = 50.0 if ara_toplam < 500 else 0.0
    
    toplam_tutar = indirimli_tutar + kargo_ucreti
    
    kullanici_tipi = sepet_verisi.get("kullanici_tipi", "")
    if kullanici_tipi == "VIP":
        toplam_tutar *= 0.90
        
    return {
        "ara_toplam": ara_toplam,
        "indirimli_tutar": indirimli_tutar,
        "kargo": kargo_ucreti,
        "toplam": toplam_tutar
    }