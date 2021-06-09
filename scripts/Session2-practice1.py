#    Generar una plantilla con variables
#    para hacerlo flexible acorde al siguiente formato:

#    - Nombre de Empresa:
#    - Objetivo:
#    - Que es lo que hace:

company_name = "Nutri-App"
company_goal = "Nutririon Consultancy"
company_role = "Provide Nutrition Consultancy and Services through our App"

string_template = f"Company Name: {company_name} Company Goal: {company_goal} Company Role: {company_role} \n"

print(string_template)

#   Lambda Function exercise
# ----------------------------------

mi_lambda = lambda x,y : x+y

var1 = "Hola"
var2 = "Mundo"

mi_lambda(var1,var2)

# Ejercicios al final de la clase:
#--------------------------------------

my_list = [10,1,"hola",3.1416,4]

# print(list(map(lambda y: str(y),my_list)))
# print(list(map(lambda y: type(y),my_list)))

list(map(lambda y: str(y),my_list))
list(map(lambda y: type(y),my_list))


