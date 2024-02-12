from agregar_eliminar_buscar_usuario import eliminar
from agregar_eliminar_buscar_usuario import registrar
from errores import error_datos
from errores import error_opcion
from ImprimirInicio import clear_console

class Administrador:
  def __init__(self, ID_administrador, Contra):
    self.ID_administrador = ID_administrador
    self.Contra = Contra

admin = Administrador("admin", "admin")

def Imprimir_Admin():
  while True:
    print("~~~~~~~~~~Bienvenido al programa: Gestión hospitalaria~~~~~~~~~~")
    print("\n")
    text = "============Administrador============"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "Administrador: *********"
    centered_text = text.center(64)
    print(centered_text)
    text = "Contraseña: *********"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "========================================"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "~~~~~~~~~~~~~~~~~~~~~~Hospital San Vicente~~~~~~~~~~~~~~~~~~~~~~"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    username = input("Ingrese ID del Administrador: ".rjust(38))
    clear_console()
    print("~~~~~~~~~~Bienvenido al programa: Gestión hospitalaria~~~~~~~~~~")
    print("\n")
    text = "============Administrador============"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "Administrador: "
    centered_text = text.rjust(31)
    print(centered_text + username)
    text = "Contraseña: *********"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "========================================"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "~~~~~~~~~~~~~~~~~~~~~~Hospital San Vicente~~~~~~~~~~~~~~~~~~~~~~"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    clave = input("Ingrese la contraseña: ".rjust(38))
    clear_console()
    print("~~~~~~~~~~Bienvenido al programa: Gestión hospitalaria~~~~~~~~~~")
    print("\n")
    text = "============Administrador============"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "Administrador: "
    centered_text = text.rjust(31)
    print(centered_text + username)
    text = "Contraseña: "
    centered_text = text.rjust(31)
    print(centered_text + clave)
    print("\n")
    text = "========================================"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "~~~~~~~~~~~~~~~~~~~~~~Hospital San Vicente~~~~~~~~~~~~~~~~~~~~~~"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    print("Presione Enter para continuar...".center(64))
    input()
    clear_console()
    
    if(admin.ID_administrador==username and admin.Contra==clave):
      
      while True:
        print("~~~~~~~~~~Bienvenido al programa: Gestión hospitalaria~~~~~~~~~~")
        print("\n")
        text = "============Administrador============"
        centered_text = text.center(64)
        print(centered_text)
        print("\n")
  
        print("1. Agregar usuario".rjust(41))
        print("2. Eliminar usuario".rjust(41))
        print("3. Cerrar sesión".rjust(40))
  
        print("\n")
        text = "========================================"
        centered_text = text.center(64)
        print(centered_text)
        
        op = int(input("Ingrese una opción: ".rjust(42)))
        print("\n")
        
        if(op == 1):
          
          id_nuevo_usuario = input("Ingrese el ID del usuario a agregar: ")
          contrasena_nuevo_usuario=input("Ingrese la contraseña de usuario a agregar: ")
          clear_console()
          registrar(id_nuevo_usuario, contrasena_nuevo_usuario)
  
        if (op == 2):
          
          eliminar_id = input("Ingrese el ID del usuario a eliminar: ")
          eliminar(eliminar_id)
          clear_console()
  
        if(op == 3):
          clear_console()
          break
            
        if(op !=1 and op !=2 and op !=3):
          error_opcion()

    else:
      error_datos()
      break
    break