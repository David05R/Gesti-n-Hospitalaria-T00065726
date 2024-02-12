from errores import error_opcion
from errores import clear_console

def menu_paciente():
  while True:
    print("~~~~~~~~~~~~~~~~Gestión hospitalaria de pacientes~~~~~~~~~~~~~~~")
    print("\n")
    text = "============Por favor seleccione una opción============"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "1. Ingresar paciente"
    centered_text = text.center(64)
    print(centered_text)
    text = "2. Actualizar datos de pacientes"
    centered_text = text.center(64)
    print(centered_text)
    text = "3. Consulta de historia clínica"
    centered_text = text.center(64)
    print(centered_text)
    text = "4. Regresar a la pagina anterior"
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

      print("Paciente")

      ##clear_console()

    if (op == 2):

      print("actualizar")
      ##clear_console()

    if(op == 3):

      print("consultar")
      ##clear_console()

    if(op == 4):

      print("regresar")
      break

    if(op !=1 and op !=2 and op !=3 and op !=4):
      error_opcion()