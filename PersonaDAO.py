from Conexion import *
from Persona import *
from Cursor import *

class PersonaDAO:
    _SELECCIONAR = "SELECT * FROM persona ORDER BY id_persona"
    _INSERTAR = "INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)"
    _ACTUALIZAR = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
    _ELIMINAR = "DELETE FROM persona WHERE id_persona=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()

            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)

            return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)

            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_persona, )
            cursor.execute(cls._ELIMINAR, valores)

            return cursor.rowcount