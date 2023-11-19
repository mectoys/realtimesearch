from src.database.connectDB import get_connection_SQLSERVER


class model_product:
    @staticmethod
    def get_products(busqueda):
        connection = get_connection_SQLSERVER()
        try:
            with connection.cursor() as cursor:
                query = "SELECT CODIGOBARRAS, NOMBRE, DESCRIPCION, UNMED FROM Productos"
                cursor.execute(query)

                result = cursor.fetchall()
                numrows = len(result)
        except Exception as e:
            print(f"Error al ejecutar la consulta: {str(e)}")
            result = []

        finally:
            connection.close()
        return result, numrows
