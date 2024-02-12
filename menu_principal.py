from errores import error_opcion
from errores import clear_console
from menu_pacientes import menu_paciente

def menu():
  while True:
    print("~~~~~~~~~~~~~~~~~~~~~~Gestión hospitalaria~~~~~~~~~~~~~~~~~~~~~~")
    print("\n")
    text = "============Por favor seleccione una opción============"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "1. Gestión de pacientes"
    centered_text = text.center(64)
    print(centered_text)
    text = "2. Reporte de indicadores"
    centered_text = text.center(64)
    print(centered_text)
    text = "3. Diagramas de camas"
    centered_text = text.center(64)
    print(centered_text)
    text = "4. Salir"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "======================================================"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "~~~~~~~~~~~~~~~~~~~~~~Hospital San Vicente~~~~~~~~~~~~~~~~~~~~~~"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    op = int(input("Ingrese una opción: ".rjust(42)))
    print("\n")
    clear_console()

    if(op == 1):

      menu_paciente()
      
      ##clear_console()

    if (op == 2):

      print("reporte")
      ##clear_console()
    
    if(op == 3):

      print("diagrama")
      ##clear_console()

    if(op == 4):

      print("salir")
      break

    if(op !=1 and op !=2 and op !=3 and op !=4):
      error_opcion()