import os
import psycopg2


configs = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

class Connector():

    @classmethod
    def conn_cur(cls):

        cls.conn = psycopg2.connect(**configs)

        cls.cur = cls.conn.cursor()

