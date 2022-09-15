print("BIENVENIDOS A MI PRIMERA TRIVIA SOBRE COMPUTACIÓN E INFORMATICA")
print("Pondremos a prueba todos tus conocimientos")
nombre= input("Ingresa tu nombre:")
edad= input("Edad:")
lugardenacimiento= input("Lugar de Nacimiento:")



print("Hola\n",nombre, "Responde las siguientes preguntas escribiendo la letra correcta con la alternativa correcta, y presiona enter para poder enviar tu respuesta:\n")

print("1) ¿Quién fue el creador de Facebook?")
print("a) Bill Gates")
print("b) Mark Zuckenberg")
print("c) Larry Page")
print("d) Peter Parker")

respuesta_1 = input("\n respuesta:")

while respuesta_1 not in("a","b","c","d"):
  respuesta_1 = input ("Debes responder a, b, c, d.Ingresa nuevamente tu respuesta:") 

if(respuesta_1 == "b"):
  print("Muy Bien!")
else:
  print("Incorrecto")


print("2) ¿Quién creó el primer algoritmo?")
print("a) Alejandro Toledo")
print("b) Elon Musk")
print("c) Ada Lovelace")
print("d) Ana Frank")

respuesta_1 = input("\n respuesta:")

while respuesta_1 not in("a","b","c","d"):
  respuesta_1 = input ("Debes responder a, b, c, d.Ingresa nuevamente tu respuesta:") 

if(respuesta_1 == "c"):
  print("Muy Bien!")
else:
  print("Incorrecto")

print("2) ¿Quién compró Twitter?")
print("a) Barack Obama")
print("b) Elon Musk")
print("c) Ada Lovelace")
print("d) Mark Zuckemberg")

respuesta_1 = input("\n respuesta:")

while respuesta_1 not in("a","b","c","d"):
  respuesta_1 = input ("Debes responder a, b, c, d.Ingresa nuevamente tu respuesta:") 

if(respuesta_1 == "b"):
  print("Muy Bien! GRACIAS POR PARTICIPAR")
else:
  print("Incorrecto GRACIAS POR PARTICIPAR")