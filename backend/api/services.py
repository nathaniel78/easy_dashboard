from django.shortcuts import get_object_or_404
from api.models import Host
import psycopg2
import mysql.connector as mysql
import logging

logger = logging.getLogger(__name__)

 # TODO: Class databaseservice
from django.shortcuts import get_object_or_404
from api.models import Host
import psycopg2
import mysql.connector as mysql
import logging

logger = logging.getLogger(__name__)

class DatabaseService:
    """
    Serviço de gerenciamento de banco de dados.
    Permite conectar e realizar consultas a bancos PostgreSQL ou MySQL.
    """
    
    def __init__(self, host_id):
        """
        Inicializa o serviço de banco de dados utilizando o Host selecionado.
        Se o host não for encontrado, as propriedades permanecem None.
        """
        self.host = None
        self.drive = None
        self.user = None
        self.password = None
        self.db_name = None
        self.port = None
        self.connection = None

        # Busca o host no banco de dados
        self._fetch_host(host_id)

    def _fetch_host(self, host_id):
        """
        Busca o host no banco de dados e inicializa as propriedades.
        """
        try:
            host = Host.objects.filter(pk=host_id).first()
            if host:
                self.host = host.host_endpoint
                self.drive = host.host_db_drive
                self.user = host.host_username
                self.password = host.host_password
                self.db_name = host.host_db_name
                self.port = host.host_port
                logger.info(f"Host {host_id} carregado com sucesso.")
            else:
                logger.warning(f"Host com ID {host_id} não encontrado.")
        except Exception as e:
            logger.error(f"Erro ao tentar carregar o host: {e}")

    def test_connection(self):
        """
        Testa a conexão ao banco de dados baseado no 'drive'.
        Retorna True se a conexão for bem-sucedida, False caso contrário.
        """
        if not self.host:
            logger.warning("Configurações do host não estão definidas. Ignorando conexão.")
            return False

        try:
            if self.drive == 1:
                self._test_postgresql_connection()
            elif self.drive == 2:
                self._test_mysql_connection()
            else:
                logger.error("Driver de banco de dados não suportado.")
                return False
        except Exception as e:
            logger.error(f"Erro ao testar a conexão: {e}")
            return False

        return True

    def _test_postgresql_connection(self):
        """
        Testa a conexão com o banco de dados PostgreSQL.
        """
        self.connection = psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            dbname=self.db_name,
            port=self.port
        )
        logger.info("Conexão com PostgreSQL bem-sucedida.")

    def _test_mysql_connection(self):
        """
        Testa a conexão com o banco de dados MySQL.
        """
        self.connection = mysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.db_name,
            port=self.port
        )
        logger.info("Conexão com MySQL bem-sucedida.")

    def execute_query(self, query):
        """
        Executa uma consulta SQL e retorna os resultados.
        """
        if not self.connection:
            logger.error("Conexão não estabelecida. Chame 'test_connection' primeiro.")
            return None

        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Exception as e:
            logger.error(f"Erro ao executar consulta: {e}")
            return None

