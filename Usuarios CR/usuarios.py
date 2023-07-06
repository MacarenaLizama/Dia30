from mysqlconnection import connectToMySQL

class Usuarios:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.fecha_creacion = data['fecha_creacion']
        self.fecha_actualizacion = data['fecha_actualizacion']

    @classmethod
    def agregar_usuario(cls, data):
        query=  """
                INSERT INTO usuarios (nombre, apellido, email)
                VALUES  (%(nombre)s, %(apellido)s, %(email)s)
                """
        resultado= connectToMySQL("bd_usuarios_cr").query_db( query, data)
        return resultado
    
    @classmethod
    def obtener_todos( cls ):
        query = """
                SELECT *
                FROM usuarios;
                """
        resultado = connectToMySQL( "bd_usuarios_cr" ).query_db( query )
        lista_usuarios = []
        
        for renglon in resultado:
            lista_usuarios.append( Usuarios( renglon ) )
        
        return lista_usuarios
    