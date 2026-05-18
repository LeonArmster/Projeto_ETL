# ===========================
# Bibliotecas
# ===========================
import pandas as pd
from config import raw_data_dir
import logging

# Extraindo dados do CSV
def extract_csv(file_name: str) -> pd.DataFrame:
    """Função para extrair dados do arquivo CSV."""
    try:
        df = pd.read_csv(raw_data_dir / file_name)
        logging.info("Dados extraídos com sucesso do CSV.")
        return df.to_csv(raw_data_dir / 'Arquivo_Processado.csv', index=False, sep=';', encoding='utf-8', lineterminator='\n')
    except Exception as e:
        logging.error(f"Erro ao extrair dados do CSV: {e}")
        raise
    

df = extract_csv('Base_2024.csv')