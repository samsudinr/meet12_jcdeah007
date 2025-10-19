import psycopg2
from psycopg2 import sql
from datetime import datetime

class PostgresConnector:
    """
    - Initialize connection to postgress
    - create table based on dataframe dtypes, and add a load_time column
    - insert table with itertuples & executemany to lessen load
    - close connection
    - wrapping create table, insert table, close connection into load function 
    """
    def __init__(self, dbname, user, password,  host = "localhost", port = 5434):
        try:
            self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
            print("Connected to postgreSQL")

        except Exception as e:
            print(f"Error Connecting: {e}")
        
    def create_table(self, table_name, dataframe):
        try:
            columns_def ={}
            for col, dtype in zip(dataframe.columns, dataframe.dtypes):
                if "object" in str(dtype):
                    columns_def[col] = "TEXT"
                elif "int" in str(dtype):
                    columns_def[col] = "BIGINT"
                elif "float" in str(dtype):
                    columns_def[col] = "FLOAT"
            columns_def["load_time"] = "TIMESTAMP DEFAULT NOW()"

            query = sql.SQL("CREATE TABLE IF NOT EXISTS {} ({})").format(
                sql.Identifier(table_name),
                sql.SQL(", ").join(sql.SQL(f"{col} {dtype}") for col, dtype in columns_def.items())
            )
            self.cursor.execute(query)

        except Exception as e:
            print(f"Error creating table: {e}")

    def insert_table(self, table_name, dataframe):
        try:
            dataframe["load_time"] = datetime.now()

            columns = list(dataframe.columns)
            query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
                sql.Identifier(table_name),
                sql.SQL(", ").join(map(sql.Identifier,columns)),
                sql.SQL(", ").join(sql.Placeholder() * len(columns))
            )

           #itertuples is faster than looping with iterrows 
            records = list(dataframe.itertuples(index = False, name = None))
            self.cursor.executemany(query, records)
            return True

        except Exception as e:
            print(f"Error Inserting: {e}")
            return False

    def close(self):
        if self.cursor and self.conn:
            self.cursor.close()
            self.conn.close()
        print(f"Connection to Postgres closed")                

    def load(self, table_name, dataframe):
        if not self.conn:
            print(f"Cannot connect to Postgres!")
            return False
        
        try:
            self.create_table(table_name, dataframe)
            print(f"{table_name} Table created successfully")

            self.insert_table(table_name, dataframe)
            print(f"Records successfully inserted to {table_name}")
            return True

        except Exception as e:
            print(f"Error creating/laoding {table_name}: {e}")
            return False
