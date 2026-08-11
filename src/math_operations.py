def hesapla_ortalama(sayilar):
    if not sayilar:
        return 0
    toplam = sum(sayilar)
    return toplam / len(sayilar)