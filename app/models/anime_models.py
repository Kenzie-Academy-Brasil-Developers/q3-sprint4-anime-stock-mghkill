from app.models import Connector
from psycopg2 import sql

class Anime(Connector):
    keys = [
        "id",
        "anime",
        "released_date",
        "seasons"
    ]

    def __init__(self, **kwargs):
        self.anime = kwargs["anime"]
        self.released_date = kwargs["released_date"]
        self.seasons = kwargs["seasons"]

    @classmethod
    def serialize(cls, data: tuple):
        return dict(zip(cls.keys, data))


    @classmethod
    def create_table(cls):
        cls.conn_cur()

        query = """
            create table if not exists animes(
	            id 				SERIAL 		 primary key,
	            anime   		VARCHAR(100) NOT NULL unique,
	            released_date   DATE 		 NOT null,
	            seasons			INTEGER 	 NOT null
            );
        """
        cls.cur.execute(query)

        cls.conn.commit()


        cls.cur.close()
        cls.conn.close()
    
    
    def create_anime(self):
        self.conn_cur()

        query = """
            insert  into animes
	            (anime, released_date, seasons)
            values
	            (%s, %s, %s)
            RETURNING *
        """

        query_values = tuple(self.__dict__.values())

        self.cur.execute(query, query_values)

        self.conn.commit()

        inserted_anime = self.cur.fetchone()

        self.cur.close()
        self.conn.close()

        return inserted_anime

  
    @classmethod
    def get_animes(cls):

        cls.conn_cur()

        query = """
            select * from animes;
        """

        cls.cur.execute(query)

        output = cls.cur.fetchall()

        cls.cur.close()
        cls.conn.close()
        

        return output

    @classmethod
    def update_animes(cls, anime_id: str, data: dict):

        cls.conn_cur()

        columns = [sql.Identifier(key) for key in data.keys()]
        values = [sql.Literal(value) for value in data.values()]
        sql_anime_id = sql.Literal(anime_id)

        query = sql.SQL(
            """
            UPDATE
                animes
            SET
                ({columns}) = ROW({values})
            WHERE
                id = {id}
            RETURNING *;
            """
        ).format(
            id=sql_anime_id,
            columns=sql.SQL(",").join(columns),
            values=sql.SQL(",").join(values),
        )
        
        cls.cur.execute(query)
        

        update_anime = cls.cur.fetchone()

        cls.conn.commit()
        cls.cur.close()
        cls.conn.close()

        return update_anime


    @classmethod
    def delete_animes(cls, anime_id):

        cls.conn_cur()

        query = sql.SQL(
        """
        DELETE FROM animes WHERE id = {id};
        """
        ).format(
            id=sql.Literal(anime_id),
        )

        cls.cur.execute(query)

        cls.conn.commit()
        cls.cur.close()
        cls.conn.close()

        