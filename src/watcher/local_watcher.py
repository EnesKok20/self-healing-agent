import subprocess
from typing import Tuple

class LocalWatcher:
    def __init__(self, target_path: str = "."):
        self.target_path = target_path

    def run_test(self) -> Tuple[bool, str]:
        try:
            print(f"🔍 [Watcher] Testler çalıştırılıyor: {self.target_path}")
            
            result = subprocess.run(
                ["pytest", self.target_path],
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=False
            )
            
            is_success = result.returncode == 0
            
            output = result.stdout + "\n" + result.stderr
            
            return is_success, output
            
        except FileNotFoundError:
            return False, "❌ Hata: 'pytest' komutu bulunamadı. Sanal ortamın (venv) aktif olduğundan emin ol."

if __name__ == "__main__":
    watcher = LocalWatcher()
    basarili_mi, cikti = watcher.run_test()
    
    print("\n--- SONUÇ ---")
    print(f"Testler Başarili mi?: {basarili_mi}")
    print(f"Hata Çiktisi:\n{cikti}")