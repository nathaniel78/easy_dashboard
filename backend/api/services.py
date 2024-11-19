from django.shortcuts import get_object_or_404
from api.models import Host
import psycopg2
import mysql.connector as mysql
import logging

logger = logging.getLogger(__name__)

class DatabaseService:
    def __init__(self, host_id):
        """
        Inicializa o serviço de banco de dados utilizando o Host selecionado.
        """
        # Busca o host no banco de dados
        host = get_object_or_404(Host, pk=host_id)
        
        if host:
            print("host already")

        # Define as propriedades de conexão a partir do serializer
        self.host = host.host_endpoint
        self.drive = host.host_db_drive
        self.user = host.host_username
        self.password = host.host_password
        self.db_name = host.host_db_name
        self.port = host.host_port
        self.connection = None

    def test_connection(self):
        """
        Testa a conexão ao banco de dados baseado no 'drive'.
        """
        try:
            if self.drive == 1:
                self._test_postgresql_connection()
            elif self.drive == 2:
                self._test_mysql_connection()
            else:
                logger.error("Driver de banco de dados não suportado.")
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
