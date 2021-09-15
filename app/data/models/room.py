from _typeshed import Self
from data.databases.conectDB import database as bd

class room:
    def create_room(self, name, sectorId):
        sql_sentence = f"""
        INSERT INTO ROOM(name, sectorId) 
        VALUES ('{name}','{sectorId}')
        """
        bd.run_sql(sql_sentence)