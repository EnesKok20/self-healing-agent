import os
import time
from google import genai
from google.genai import errors
from typing import Dict, Optional

class ReasonerAgent:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError(" Hata: GEMINI_API_KEY bulunamadı! .env dosyasını kontrol et.")
            
        self.client = genai.Client(api_key=self.api_key)
        
        # Sabit sürüm adlari yeni hesaplar için kapatilabiliyor;
        # Google'in hep güncel tuttuğu alias'i kullaniyoruz.
        self.model_name = "gemini-flash-latest"

    def generate_patch(self, error_details: Dict[str, str], code_snippet: str) -> Optional[str]:
        prompt = f"""
        Sen otonom bir Python hata ayıklama ajanısın. Aşağıdaki hatalı Python kodunu düzelt.
        Sadece düzeltilmiş saf Python kodunu ver, başka hiçbir açıklama veya markdown ekleme.
        
        Hatalı Kod:
        {code_snippet}
        """
        
        max_deneme = 3
        bekleme = 2  # saniye, her denemede iki katına çıkar

        for deneme in range(1, max_deneme + 1):
            try:
                print(f" [Reasoner] Gemini kodu analiz edip yama üretiyor... (deneme {deneme}/{max_deneme})")

                # Doğrudan model çağrısı
                response = self.client.models.generate_content(
                    model=self.model_name,
                    contents=prompt
                )

                return response.text.strip()

            except errors.ServerError as e:
                # 500/503 gibi geçici sunucu hataları: tekrar dene
                print(f" [Reasoner] Sunucu hatası (geçici olabilir): {e}")
                if deneme < max_deneme:
                    time.sleep(bekleme)
                    bekleme *= 2
                else:
                    return None

            except Exception as e:
                # 404 gibi kalıcı hatalar: tekrar denemenin anlamı yok
                print(f" [Reasoner] API Hatası: {e}")
                return None

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    ornek_hata = {
        "file_path": "tests/test_dummy.py",
        "line_number": "3",
        "error_type": "AssertionError"
    }
    ornek_kod = "def test_bilerek_hata_ver():\n    assert 1 == 2"
    
    ajan = ReasonerAgent()
    cozum = ajan.generate_patch(ornek_hata, ornek_kod)
    
    print("\n--- GEMINI (YAPAY ZEKA) ÇÖZÜMÜ ---")
    print(cozum)