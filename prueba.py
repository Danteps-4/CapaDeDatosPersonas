from Persona import Persona
from PersonaDAO import PersonaDAO
from Conexion import Conexion
from logger_base import log
    
# Insertar persona
# persona1 = Persona(nombre="Pepito", apellido="Rodriguez", email="pepito@gmail.com")
# insertadas = PersonaDAO.insertar(persona1)
# log.debug(f"Personas insertadas: {insertadas}")

# Actualizar persona
# persona1 = Persona(15, "Jorje", "Juarez", "jorgito@hotmail.com")
# acutalizados = PersonaDAO.actualizar(persona1)
# log.debug(f"Personas actualizadas: {acutalizados}")

# Eliminar persona
# persona1 = Persona(id_persona=14)
# eliminados = PersonaDAO.eliminar(persona1)
# log.debug(f"Personas eliminadas: {eliminados}")

# Seleccionar todas las personas
personas = PersonaDAO.seleccionar()
for persona in personas:
    print(persona)