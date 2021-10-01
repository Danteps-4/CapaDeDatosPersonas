from Conexion import *
from Persona import *

class PersonaDAO:
    _SELECCIONAR = "SELECT * FROM persona ORDER BY id_persona"
    _INSERTAR = "INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)"
    _ACTUALIZAR = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
    _ELIMINAR = "DELETE FROM persona WHERE id_persona=%s"

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()

                personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)

                return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)

                return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona, )
                cursor.execute(cls._ELIMINAR, valores)

                return cursor.rowcount

if __name__ == "__main__":
    #Insertar persona
    # persona1 = Persona(nombre="Pepito", apellido="Genitales", email="pepito@gmail.com")
    # insertadas = PersonaDAO.insertar(persona1)
    # log.debug(f"Personas insertadas: {insertadas}")

    #Actualizar persona
    # persona1 = Persona(15, "Jorgitooo", "Juarez", "jorgiño@hotmail.com")
    # acutalizados = PersonaDAO.actualizar(persona1)
    # log.debug(f"Personas actualizadas: {acutalizados}")

    #Eliminar persona
    # persona1 = Persona(id_persona=14)
    # eliminados = PersonaDAO.eliminar(persona1)
    # log.debug(f"Personas eliminadas: {eliminados}")

    # Seleccionar todas las personas
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        print(persona)