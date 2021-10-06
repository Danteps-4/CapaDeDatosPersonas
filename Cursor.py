from logger_base import log
from Conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detaller_excepcion):
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f"Ocurrio un error: {valor_excepcion}")
        else:
            self._conexion.commit()
            log.debug("Commit de la transaccion")
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)


if __name__ == "__main__":
    with CursorDelPool() as cursor:
        cursor.execute("SELECT * FROM persona")
        log.debug(cursor.fetchall())