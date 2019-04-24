#Programa que te dice que nota tienes y si el dato es mayor o fuera de rango, manda un error

print("\nPuntuación\tClasificación\n>=0.9\t\tSobresaliente\n>=0.8\t\tNotable\n>=0.7\t\tBien\n>=0.6\t\tSuficiente\n< 0.6\t\tInsuficiente\n")
       
try:
    puntuacion=float(input(("Escribe tu puntuación: ")))
#si la puntación es mayor que 1.0 se ejecuta este if dando el error
    if puntuacion > 1.0:
       print("Puntuación incorrecta, elige un rango válido entre 0.0 y 1")
#si el dato esta bien se ejecuta este bloque
    elif puntuacion < 0.6:
          print("Insuficiente")
    elif puntuacion >= 0.6 and puntuacion < 0.7:
          print("Suficiente")
    elif puntuacion >= 0.7 and puntuacion < 0.8:
          print("Bien")
    elif puntuacion >= 0.8 and puntuacion  < 0.9:
          print("Notable")
    elif puntuacion >= 0.9:
          print("Sobresaliente")
#si el dato no es el que se espera sale este error
except:
	print("Dato incorrecto, inténtalo de nuevo")