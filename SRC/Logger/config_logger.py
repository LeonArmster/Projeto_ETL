# ==================================
# Biblioteca
# ==================================
import logging
import pandas as pd
from logging.handlers import RotatingFileHandler
from config import sql, log_dir
from sqlmodel import text

# Criando a função para confugurar o logger
def configure_logger():
    """Configura o logger para o projeto ETL."""

    # Configuração do logger
    log_path = log_dir / 'etl_log.log'

    # Criando conector do lo
    logger = logging.getLogger()

    # Definindo o nível de log
    logger.setLevel(logging.INFO)

    # Configurando a gestão do logger para evitar múltiplos handlers
    if not logger.handlers:
        # Criando um manipulador de arquivo rotativo
        handler = RotatingFileHandler(log_path, maxBytes=5*1024*1024, backupCount=5)

        # Definindo o formato do log
        formato_log = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Aplicando a formatação ao manipulador e adicionando ao logger
        handler.setFormatter(formato_log)

        # Adicionando o manipulador ao logger
        logger.addHandler(handler)