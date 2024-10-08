import mysql.connector
import config

class DatabaseManager:
    _singleton_instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton_instance:
            cls._singleton_instance = super(DatabaseManager, cls).__new__(cls)
        return cls._singleton_instance

    def __init__(self):
        if not hasattr(self, 'conn'):
            self.conn = mysql.connector.connect(
                host="localhost",
                user=config.DB_USER,
                password=config.DB_PASSWORD,
                database='restaurant_db'
            )
            self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def execute_query(self, sql_query=None, file_path=None):
        results = []
        if file_path:
            with open(file_path, 'r') as f:
                sql_query = f.read()
        commands = sql_query.split(';')
        for command in commands:
            command = command.strip()
            if command:
                try:
                    self.cursor.execute(command)
                    if command.lower().startswith("select"):
                        results.append(self.cursor.fetchall())
                    else:
                        self.conn.commit()
                except Exception as e:
                    results.append(f"Execution Error: {e}")
                    self.conn.rollback()
        return results

    def initialize_database(self):
        self.execute_query(file_path="databaseCreation.sql")
        self.execute_query(file_path="tableCreation.sql")
        self.conn.commit()
