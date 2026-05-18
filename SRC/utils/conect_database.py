# ===================================
# Configurando conexão com o banco de dados
# ===================================
# Bibliotecas
from sqlmodel import create_engine
from config import server, database, username, password, port, sql_dir

# Função para conectar ao banco de dados
def connect_database():
    """Função para criar a conexão com o banco de dados SQL Server usando SQLModel."""
    connection_string = (
        f'mssql+pyodbc://{username}:{password}'
        f'@{server}:{port}/{database}'
        '?driver=ODBC+Driver+17+for+SQL+Server'
    )

    engine = create_engine(connection_string, fast_executemany=True)

    return engine

# Função para ler query
def read_query(file_name: str) -> str:
    """
    Função para ler uma query SQL de um arquivo.
    
    Parametros:
    file_name: Nome do arquivo SQL a ser lido. O arquivo deve estar localizado no diretório sql_dir.
    """
    with open(file=sql_dir/file_name, mode='r') as file:
        query = file.read()
    return query