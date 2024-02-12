from ImprimirInicio import clear_console
from ImprimirInicio import imprimir_Inicio_Sesion
from Admin import Imprimir_Admin
from errores import error_opcion
from menu_principal import menu

TypeU = 0

while True:
  print("~~~~~~~~~~Bienvenido al programa: Gestión hospitalaria~~~~~~~~~~")
  print("\n")
  text = "============Inicio de sesión============"
  centered_text = text.center(64)
  print(centered_text)
  print("\n")
  print("Digite el tipo de usuario:".rjust(46))
  print("1. Administrador".rjust(40))
  print("2. Normal".rjust(36))
  print("\n")
  text = "========================================"
  centered_text = text.center(64)
  print(centered_text)
  print("\n")
  text = "~~~~~~~~~~~~~~~~~~~~~~Hospital San Vicente~~~~~~~~~~~~~~~~~~~~~~"
  centered_text = text.center(64)
  print(centered_text)
  print("\n")
  TypeU = input("Ingrese Tipo de Usuario: ".rjust(43))
  clear_console()

  if(TypeU == "1"):
    Imprimir_Admin()
    
  if(TypeU == "2"):
    imprimir_Inicio_Sesion()
    
  if(TypeU != "1" and TypeU != "2"):
    error_opcion()    