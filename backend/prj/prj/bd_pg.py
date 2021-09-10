from psycopg2 import OperationalError
import psycopg2

def __init__(self, codepoint_dir = '.'):
    self._db = connect_database()

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


connection = create_connection(
    "skillfactory", "skillfactory", "cCkxxLVrDE8EbvjueeMedPKt", "127.0.0.1", "5432"
)

create_database_query = "CREATE DATABASE zalivki"
create_database(connection, create_database_query)
connection = create_connection(
    "zalivki", "postgres", "1111", "127.0.0.1", "5432"
)