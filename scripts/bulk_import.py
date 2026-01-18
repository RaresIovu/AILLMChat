print("--- SCRIPTUL A PORNIT ---")
import sys
import os
import json
import logging
from pathlib import Path

# Adaugă directorul rădăcină în path
sys.path.insert(0, str(Path(__file__).parent.parent))

from knowledge.service import add_knowledge

# Configurarea logging se pune de obicei la început, în afara funcțiilor
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def import_from_json(file_path):
    logging.info(f"Încep importul din fișierul: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        count = 0
        for item in data:
            subject = item.get('subject')
            grade = item.get('grade')
            content = item.get('content')
            
            if not (subject and grade and content):
                logging.warning(f"Element sărit (date incomplete): {item}")
                continue
            
            add_knowledge(subject, grade, content)
            count += 1
            if count % 5 == 0:
                logging.info(f"Am importat {count} elemente...")
        
        logging.info(f"Succes! S-au importat în total {count} lecții.")
        return count
    
    except Exception as e:
        logging.error(f"Eroare critică la import: {e}")
        return 0

# --- ACEASTA ESTE PARTEA CARE LIPSEA ---
if __name__ == "__main__":
    # Verificăm dacă ai dat un argument în linia de comandă (numele fișierului)
    if len(sys.argv) > 1:
        fisier = sys.argv[1]
        import_from_json(fisier)
    else:
        logging.error("Nu ai specificat fișierul JSON! Folosește: python scripts/bulk_import.py knowledge_data.json")