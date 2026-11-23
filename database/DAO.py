from database.DB_connect import DBConnect
from model.luogo import Luogo


class DAO:
    @staticmethod
    def read_all_luoghi():
        conn = DBConnect.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            try:
                cursor.execute("SELECT id, nome, tipo, quota_m FROM luogo ORDER BY id")
                result = []
                for row in cursor:
                    luogo = Luogo(row["id"], row["nome"], row["tipo"], row["quota_m"])
                    result.append(luogo)
                return result
            finally:
                cursor.close()
        finally:
            conn.close()

    @staticmethod
    def check_if_u_and_v_connected(u : int, v : int):


        def read_all_luoghi():
            conn = DBConnect.get_connection()
            try:
                cursor = conn.cursor(dictionary=True)
                try:
                    query = ("SELECT * FROM sentiero "
                                   "WHERE id_luogo_1 = %s AND id_luogo_2 = %s ")
                    cursor.execute(query, (u, v))
                    result = []
                    for row in cursor:
                        result.append(row)
                    return result
                finally:
                    cursor.close()
            finally:
                conn.close()