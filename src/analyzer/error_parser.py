import re
from typing import Dict, Optional

class ErrorParser:
    def __init__(self):
        # pytest hata formatini (dosya.py:satir: HataTipi) yakalamak için Regex kalibi
        self.error_pattern = re.compile(r"([a-zA-Z0-9_/\\]+\.py):(\d+): (.+)")

    def parse(self, error_log: str) -> Optional[Dict[str, str]]:
        """
        Logu inceler ve dosya, satır no, hata tipini sözlük olarak döner.
        """
        # Gelen devasa log metnini satır satır bölüp inceliyoruz
        for line in error_log.split('\n'):
            match = self.error_pattern.search(line)
            if match:
                return {
                    "file_path": match.group(1).strip(),
                    "line_number": match.group(2).strip(),
                    "error_type": match.group(3).strip()
                }
        
        # Eğer logun içinde standart bir hata formatı bulamazsak None dönüyoruz
        return None

if __name__ == "__main__":
    # Analyzerin doğru çalişip çalişmadiğini küçük bir log ile test edelim
    ornek_log = """
    ================================== FAILURES ===================================
    ____________________________ test_bilerek_hata_ver ____________________________
    assert 1 == 2
    E       assert 1 == 2
    tests/test_dummy.py:3: AssertionError
    =========================== short test summary info ===========================
    """
    
    parser = ErrorParser()
    sonuc = parser.parse(ornek_log)
    
    print("\n--- ANALİZ SONUCU ---")
    print(sonuc)