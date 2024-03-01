##crear un programa que simulle la entrada a un boliche. Debe dejar ingresar la edad del usuario, si es mayor a 18 mostrar por pantalla "puede ingresar", de lo contrario mostrar por pantalla "no puede entrar"
edad = int(input("por favor ingrese su edad: "))
if edad <= 18:
  print("puede ingresar")
else:
  print("lo siento, no puede ingresar")
