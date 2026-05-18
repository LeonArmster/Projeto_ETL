# ==============================
# Configurações para Bulk Insert
# ==============================
# Bibliotecas
from config import raw_data_dir, arquivo_docker
from utils.conect_database import read_query, connect_database
from sqlmodel import text
import logging

# Função para realizar o bulk insert
# # conectando ao banco
# engine = connect_database()

# # Tabela que será carregado
# tabela = 'Treinamento.DBO.Stg_Tb_Efetividade_Geral'



def executar_bulk_insert(engine, query:str, tabela:str, arquivo:str):
    """
    Função para executar o bulk insert no banco de dados.

    Parâmetros:
    - engine: Conexão com o banco de dados.
    - query: Query de bulk insert a ser executada.
    - tabela: Nome da tabela onde os dados serão inseridos.
    - arquivo: Caminho do arquivo CSV a ser carregado.
    #### Exemplo de arquivo
    ##### arquivo = (arquivo_docker/'Arquivo_Processado.csv').as_posix()

    Retorna:
    - None: A função não retorna nenhum valor, mas executa o bulk insert no banco de dados.
    """

    # Arquivo que será carregado
    arquivo = (arquivo).as_posix()

    # Exemplo de arquivo
    # arquivo = (arquivo_docker/'Arquivo_Processado.csv').as_posix()

    # Nome da query
    query = read_query(query)

    # Configurando a query com os parâmetros
    query = query.format(tabela=tabela, arquivo=arquivo)

    # Conectando ao banco
    with engine.begin() as conexao:

        # Realizando o bulk insert
        try:
            logging.info("Iniciando o Bulk Insert.")
            conexao.execute(text(query))
            logging.info("Bulk insert realizado com sucesso.")

        # Caso ocorra algum erro, ele será logado e a exceção será levantada
        except Exception as e:
            logging.error(f"Erro ao realizar bulk insert: {e}")
            raise
