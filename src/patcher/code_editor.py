import os

class CodePatcher:
    def __init__(self):
        pass

    def apply_patch(self, file_path: str, patched_code: str) -> bool:
        """
        Yapay zekanin ürettiği yeni kodu, hedef dosyanin üzerine yazar.
        """
        try:
            print(f"[Patcher] Yama uygulaniyor: {file_path}")
            
            
            if not os.path.exists(file_path):   #hedefteki dosyanin var olup olmadiğini kontrol eder.
                print(f"[Patcher] Hata: {file_path} dosyasi bulunamadi!")
                return False
                
            # Temizlenmiş kodu dosyaya yaz
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(patched_code)
                
            print(f"[Patcher] Yama başariyla uygulandi ve kaydedildi: {file_path}")
            return True
            
        except Exception as e:
            print(f"[Patcher] Dosya Yazma Hatasi: {e}")
            return False

if __name__ == "__main__":
    # Test amaçli geçici bir dosya üzerinde patcher'i test edelim
    test_dosya = "tests/test_dummy.py"
    
    # Yapay zekanin ürettiğini varsaydiğimiz düzeltilmiş kod
    ornek_yeni_kod = "def test_bilerek_hata_ver():\n    assert 1 == 1"
    
    patcher = CodePatcher()
    basarili_mi = patcher.apply_patch(test_dosya, ornek_yeni_kod)
    
    print("\n--- PATCHER TEST SONUCU ---")
    print(f"Yama Uygulandi  mi?: {basarili_mi}")