# ===================================
# Projeto ETL - Extração, Transformação e Carga de Dados
# ===================================
# Bibliotecas
from Extract.extract_csv import extract_csv
from Load.bulk_insert import executar_bulk_insert
from Load.truncate_table import executar_truncate_table
from Logger.config_logger import configure_logger
from utils.conect_database import connect_database
from config import arquivo_docker
import logging


def main():
    # Configurando o Logger
    configure_logger()
    logging.info("Iniciando o processo ETL.")

    # Conectando ao banco de dados
    logging.info("Estabelecendo conexão com o banco de dados.")
    engine = connect_database()
    logging.info("Conexão com o banco de dados estabelecida com sucesso.")

    # Transformando os dados do csv para inserção correta no banco
    extract_csv('Base_2024.csv')

    # Tabela principal onde os dados serão inseridos
    tabela = 'Treinamento.DBO.Stg_Tb_Efetividade_Geral'

    # Query de truncate table
    query = 'truncate.sql'

    # Executando o Truncate Table
    executar_truncate_table(engine, query, tabela)

    # Query de bulk insert
    query = 'bulk_insert.sql'

    # Caminho do arquivo processado para o bulk insert
    arquivo = (arquivo_docker/'Arquivo_Processado.csv').as_posix()

    # Executando o Bulk Insert
    executar_bulk_insert(engine, query, tabela, arquivo)



if __name__ == "__main__":
    main()