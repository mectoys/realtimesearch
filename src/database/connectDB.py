import pyodbc
import os
from dotenv import  load_dotenv

load_dotenv("parameters.env")


def get_connection_SQLSERVER():
    try:
        connection_string = (
            f"DRIVER={os.getenv('SQL_SERVER_DRIVER')};"
            f"SERVER={os.getenv('SQL_SERVER_SERVER')};"
            f"DATABASE={os.getenv('SQL_SERVER_DATABASE')};"
            f"UID={os.getenv('SQL_SERVER_UID')};"
            f"PWD={os.getenv('SQL_SERVER_PWD')}"
        )
        connection = pyodbc.connect(connection_string)
        return connection
    except Exception as e:
        print("Error de conexion " + e)
        return None
