class Suma:
  
    def operar(self, num1, num2):
        return num1 + num2  # Retorna la suma de num1 y num2


class Resta:
    
    def operar(self, num1, num2):
        return num1 - num2  # Retorna la resta de num1 menos num2


class Multiplicacion:
   
    def operar(self, num1, num2):
        return num1 * num2  # Retorna el producto de num1 y num2

class Division:
    
    def operar(self, num1, num2):
        # Verifica si el divisor es 0,para no realizar esta operacion
        if num2 == 0:
            return "error"  # Si el divisor es 0, retorna un mensaje de error
        return num1 / num2  # Si no existe un error, retorna el cociente de num1 y num2


class Exponencial:
    
    def operar(self, base, exponente):
        return base ** exponente  # Retorna la base elevada al exponente
