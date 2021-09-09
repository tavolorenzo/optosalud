import sqlite3

class database:
    url_database = '../../optosalud.db'

    def _open_conection(self):
        try:
            self.conexion = sqlite3.connect(database.url_database)
        except Exception as e:
            print(e)

    def _close_conection(self):
        self.conexion.close()
        self.conexion = None

    def run_sql(self, sql):
        self._open_conection()
        cur = self.conexion.cursor()
        cur.execute(sql)

        rows = cur.fetchall()

        self.conexion.commit()
        self._close_conection()

        return rows
