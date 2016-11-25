from usuario import Usuario

user = Usuario()

print (type(user))
print("Nombre del usuario antes de peticion")
print(user.nombre)

respuesta = user.obtenerInformacion()

message = input ("introduce tu mensaje: ")
user.publicarComentario(message)

print ("hice un cambio")