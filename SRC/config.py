# ==============================
# Configurações do projeto
# ==============================
# Bibliotecas
import os
from pathlib import Path
from dotenv import load_dotenv

# Configuração de variáveis de ambiente
load_dotenv()

server = os.getenv('servidor')
database = os.getenv('database')
username = os.getenv('login')
password = os.getenv('senha')
port = os.getenv('porta')

# Configurações de diretórios
base_dir = Path(__file__).resolve().parent.parent
data_dir = base_dir / 'Data'
image_dir = base_dir / 'Images'
raw_data_dir = data_dir / 'raw'
processed_data_dir = data_dir / 'processed'
sql_dir = base_dir / 'SQL'
log_dir = data_dir / 'log'

# Diretorio docker
arquivo_docker = Path('/data/raw/')


