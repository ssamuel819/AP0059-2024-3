# Importamos las clases Suma, Resta, Multiplicacion, Division y Exponencial desde el archivo 'Calculadora'
from Calculadora import Suma
from Calculadora import Resta
from Calculadora import Multiplicacion
from Calculadora import Division
from Calculadora import Exponencial

# Definimos la función principal main que contiene el bucle de la calculadora
def main():
  print ("Abriendo calculadora")
    
  
    while True:

        # Muestra las multiples opciones al usuario
        print("Selecciona la operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Exponencial")
        print("6. Salir")
        
        opcion = input("Elige una opción (1-6): ")
        
        
        if opcion == '6':
            print("Saliendo de la calculadora.")  
            break  # Al escoger el numero 6 el bucle terminara y se saldra de la calculadora

        
        num1 = float(input("Introduce el primer número: "))
        
     
        if opcion == '5':
            num2 = float(input("Introduce el exponente: "))  
        else:
            num2 = float(input("Introduce el segundo número: "))  

        
        if opcion == '1':
            operacion = Suma()  
        elif opcion == '2':
            operacion = Resta()  
        elif opcion == '3':
            operacion = Multiplicacion()  
        elif opcion == '4':
            operacion = Division()  
        elif opcion == '5':
            operacion = Exponencial()  
        else:
           
            print("Opción no válida")  # Si se ingresa una opción no válida, se muestra un mensaje de error y continúa el bucle
            continue  

        
        resultado = operacion.operar(num1, num2)
        
        print(f"El resultado es: {resultado}")
        

if __name__ == "__main__":
    main()
