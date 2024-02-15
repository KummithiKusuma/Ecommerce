import psycopg2  # Assuming PostgreSQL database

class DBConnUtil:
    @staticmethod
    def get_connection(connection_string: str):
        # Establish a database connection and return the connection object
        return psycopg2.connect(connection_string)
