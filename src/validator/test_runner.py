import subprocess
from typing import Tuple

class PatchValidator:
    def __init__(self, target_path: str = "."):
        self.target_path = target_path

    def validate_patch(self) -> Tuple[bool, str]:
        """
        Yama uygulandiktan sonra testleri tekrar calistirarak dogrular.
        """
        try:
            print(f"[Validator] Testler dogrulaniyor: {self.target_path}")
            
            result = subprocess.run(
                ["pytest", self.target_path],
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=False
            )
            
            is_success = result.returncode == 0
            output = result.stdout + "\n" + result.stderr
            
            if is_success:
                print("[Validator] Dogrulama Basarili! Testler gecti.")
            else:
                print("[Validator] Dogrulama Basarisiz! Testler hala hata veriyor.")
                
            return is_success, output
            
        except FileNotFoundError:
            return False, "[Hata] 'pytest' komutu bulunamadi."

if __name__ == "__main__":
    validator = PatchValidator()
    basarili_mi, cikti = validator.validate_patch()
    
    print("\n--- VALIDATOR TEST SONUCU ---")
    print(f"Testler Gecti mi?: {basarili_mi}")
    print(f"Test Ciktisi:\n{cikti}")