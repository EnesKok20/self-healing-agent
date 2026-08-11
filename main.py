import os
from dotenv import load_dotenv

from src.watcher.local_watcher import LocalWatcher
from src.analyzer.error_parser import ErrorParser
from src.reasoner.agent import ReasonerAgent
from src.patcher.code_editor import CodePatcher
from src.validator.test_runner import PatchValidator

class SelfHealingAgent:
    def __init__(self, max_retries: int = 3):
        load_dotenv()
        self.max_retries = max_retries
        
        # Modulleri baslatiyoruz
        self.watcher = LocalWatcher()
        self.parser = ErrorParser()
        self.reasoner = ReasonerAgent()
        self.patcher = CodePatcher()
        self.validator = PatchValidator()

    def run(self):
        print("[Agent] Self-Healing Agent baslatildi.")
        
        for attempt in range(1, self.max_retries + 1):
            print(f"\n--- DENEME {attempt} / {self.max_retries} ---")
            
            # 1. Adim: Testleri calistir ve hata var mi bak
            is_success, log_output = self.watcher.run_test()
            
            if is_success:
                print("[Agent] Tum testler basarili! Iyilestirilecek bir hata yok.")
                return True
                
            print("[Agent] Basarisiz testler tespit edildi, analiz basliyor...")
            
            # 2. Adim: Hatayi analiz et (Dosya ve satir no bul)
            error_details = self.parser.parse(log_output)
            if not error_details:
                print("[Hata] Log icinde standart hata formati bulunamadi.")
                return False
                
            print(f"[Agent] Hata Analiz Edildi: {error_details}")
            
            # Hata dosyasinin icindeki hatali kodu oku
            target_file = error_details.get("file_path")
            if not os.path.exists(target_file):
                print(f"[Hata] Hedef dosya bulunamadi: {target_file}")
                return False
                
            with open(target_file, "r", encoding="utf-8") as f:
                code_snippet = f.read()
                
            # 3. Adim: Reasoner ile yapay zekadan yama iste
            patched_code = self.reasoner.generate_patch(error_details, code_snippet)
            if not patched_code:
                print("[Hata] Yapay zeka yama uretemedi.")
                continue
                
            # Markdown blok temizligi (Eger yapay zeka ```python ... ``` eklediyse temizle)
            if patched_code.startswith("```"):
                lines = patched_code.splitlines()
                if lines[0].startswith("```"):
                    lines = lines[1:]
                if lines and lines[-1].startswith("```"):
                    lines = lines[:-1]
                patched_code = "\n".join(lines).strip()
                
            # 4. Adim: Patcher ile yamayi dosyaya uygula
            patch_applied = self.patcher.apply_patch(target_file, patched_code)
            if not patch_applied:
                print("[Hata] Yama dosyaya uygulanamadi.")
                continue
                
            # 5. Adim: Validator ile yamadan sonra testleri tekrar dogrula
            validation_success, _ = self.validator.validate_patch()
            if validation_success:
                print("[Agent] Harika! Ajan kodu basariyla iyilestirdi ve testler gecirildi.")
                return True
            else:
                print("[Agent] Yama uygulandi ancak testler hala gecmedi. Dongu tekrarlaniyor...")
                
        print("[Agent] Maksimum deneme sinirina ulasildi, hata otomatik olarak giderilemedi.")
        return False

if __name__ == "__main__":
    agent = SelfHealingAgent()
    agent.run()