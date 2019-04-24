Algoritmo escentral
	Definir num1 Como Entero
	Definir num2 Como Entero
	Definir num3 Como Entero
	Escribir "Escribe numeros por favor"
	Leer num1
	Leer num2
	Leer num3
	numero1 <- num1
	numero2 <- num2
	numero3 <- num3
	
	Si numero1 es mayor que numero2 Y numero1 es menor que numero3 o num1 es menor que num2 y num1 es mayor que num3 Entonces
		Escribir 'El numero central es ',numero1
	FinSi
	Si numero2 es mayor que numero1 Y numero2 es menor que numero3 o num2 es menor que num1 y num2 es mayor que num3 entonces
		Escribir 'El numero central es ',numero2
	FinSi
	Si numero3 es mayor que num1 y num3 es menor que num2 o num3 es menor que num1 y num3 es mayor que num2
		Escribir 'El numero central es ',numero3
	FinSi
	
	si num1 es igual a num2 o num2 es igual a num3 o num1 es igual a num3 o num1 es igual a num2 y num1 es igual a num3 Entonces
		Escribir 'No hay central, hay uno o mas numeros iguales'
	FinSi
FinAlgoritmo

//5,3,6