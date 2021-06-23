"""
    Crear una clase que tenga un método llamado pedir_input, esa función pedira
    un número al usuario y no lo dejará de molestar hasta que su input sea correcto
    (ValueError:)
    Si ese número es par dividirlo por 10, si no dividirlo por 0 y manda el mensaje
    el sistema no pudo calcular la división
"""

class myError_Handler():
    def __init__(self):
        self.user_input = 0

    def get_userInput(self):
        
        try:
            self.user_input = float(input("Please provide a number to do calculations --- "))
        except Exception as myerr:            
            print("Please provide a number in order to follow to calculations --- ") 
            self.get_userInput()
        else:
            self.data_calculation()
        finally:
            print(f'The detected error was: {myerr.__traceback__}')
            print("The method get_user_input has finished")

    def data_calculation(self):

        try:
            if self.user_input %2 == 0:
                self.user_input /= 10 
            else:
                self.user_input /= 0
        except Exception as myerr:
            print(f'The current error is: {myerr}')
            print("System has been not able to execute the operation =(")
        else:
            print(f'Everything has been worked well the result is: {self.user_input}')
        finally:
            print("The method data_calculation has finished")
            # Ejemplo: matar todas las conexiones o cerrarlas

myError = myError_Handler()
myError.get_userInput()
