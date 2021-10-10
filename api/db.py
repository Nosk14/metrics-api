import psycopg2


class DBClient:

    def __init__(self, host, dbname, user, password):
        self.__conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
        self.__create_orchard_table()
        self.__conn.commit()

    def __create_orchard_table(self):
        self.__conn.execute("""CREATE TABLE IF NOT EXISTS orchard (
            name VARCHAR(32) NOT NULL,
            humidity REAL NOT NULL,
            instant TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
        );""")

    def store_orchard_data(self, name, humidity):
        cursor = self.__conn.cursor()
        cursor.execute("INSERT INTO orchard (name, humidity) VALUES (%s, %s)", name, humidity)
        cursor.commit()
        cursor.close()
