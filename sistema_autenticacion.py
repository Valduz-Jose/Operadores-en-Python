# Sistema de Autenticacion

print("*****Sistema de Autenticacion*****")
usuario = input("Proporciona tu nombre de usuario: ")
password = input("Proporciona tu contraseña: ")
# Verificar si el usuario y contraseña son correctos
USUARIO_CORRECTO = "admin"
PASSWORD_CORRECTO = "1234" 

autenticacion_exitosa = (usuario == USUARIO_CORRECTO) and (password == PASSWORD_CORRECTO)

print(f"¿La autenticación fue exitosa? {autenticacion_exitosa}")