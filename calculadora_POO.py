class Calculadora:
    
    def __init__(self, numero1, numero2):
        self._numero1 = numero1
        self._numero2 = numero2
        self._historial = []

    @property
    def numero1(self):
        return self._numero1

    @numero1.setter
    def numero1(self, nuevo_numero1):
        if type(nuevo_numero1) in (int, float):
            self._numero1 = nuevo_numero1
        else:
            raise ValueError("Debe ser un numero")

    @property
    def numero2(self):
        return self._numero2

    @numero2.setter
    def numero2(self, nuevo_numero2):
        if type(nuevo_numero2) in (int, float):
            self._numero2 = nuevo_numero2
        else:
            raise ValueError("Debe ser un numero")

    def sumar(self):
        resultado = self._numero1 + self._numero2
        self.registrar_operacion('+', resultado)  
        return resultado
    
    def restar(self):
        resultado=self._numero1-self._numero2
        self.registrar_operacion('-', resultado)
        return resultado
    
    def multiplicar(self):
        resultado=self._numero1*self._numero2
        self.registrar_operacion('*', resultado)
        return resultado
    
    def dividir(self):
        resultado=self._numero1/self._numero2
        self.registrar_operacion('/', resultado)
        return resultado

    def registrar_operacion(self, operador, resultado): 
        self._historial.append({
            'operacion': f"{self._numero1} {operador} {self._numero2}",
            'resultado': resultado
        })

    def ver_historial(self):
        if not self._historial:
            print("No hay operaciones en el historial.")
            return

        print("\n---Historial de Operaciones---")
        contador = 1
        for operacion in self._historial:
            print(f"{contador}. {operacion['operacion']} = {operacion['resultado']}")
            contador += 1


def interpretar_expresion(expresion):
    """Interpreta la expresion matematica ingresada"""
    for operador in ['+', '-', '*', '/']:
        if operador in expresion:
            partes = expresion.split(operador)
            if len(partes) == 2:
                num1_str = partes[0].strip() #Quitamos el float y devolvemos las cadenas
                num2_str = partes[1].strip()
                return num1_str, num2_str, operador


def main():
    calc = Calculadora(0, 0)
    print("Calculadora Basica. Puedes continuar haciendo operaciones o  Escribe 'salir' para termiar o 'historial' para ver operaciones.\n")

    while True:
        entrada = input("Ingresa la operacion(ejemplo:5+5): ") 

        if entrada.strip().lower() == "salir":
            print("Hasta Pronto!")
            break

        if entrada.strip().lower() == "historial":
            calc.ver_historial()
            continue

        resultado = interpretar_expresion(entrada)
        if not resultado:
            print("Expresion no valida. Usa el formato: numero operador numero(ej. 5+5)\n")
            continue

        num1_str, num2_str, operador = resultado
        try:#Ejecuta codigo riesgoso
            #Convertimos la cadena de texto  a numero(float)
            num1=float(num1_str)
            num2=float(num2_str)
            #Asignamos llamando a los setters
            calc.numero1=num1
            calc.numero2= num2
            #Realizamos la operacion
            match operador:
                case '+':
                    print("Resultado:", calc.sumar())
                case "-":
                    print("Resultado:", calc.restar())   
                case '*':
                    print("Resultado:", calc.multiplicar())  
                case "/":
                    print("Resultado:", calc.dividir())     
        except ValueError:#Define si ese riesgo se materializa 
            #Captura el error con letras 
            print("Error:Debe ser un numero\n")
        except ZeroDivisionError:
            #Captura el error al intentar dividir entre 0
            print("Error: No se puede dividir por cero.\n")

main()



        