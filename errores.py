import os

def clear_console():
  os.system('cls' if os.name == 'nt' else 'clear')

def error_opcion():
  print("~~~~~~~~~~~~~~~~~~~~~~Gestión hospitalaria~~~~~~~~~~~~~~~~~~~~~~")
  print("\n")
  text = "============Error de selección============"
  centered_text = text.center(64)
  print(centered_text)
  print("\n")
  print("Error: Opción inválida".center(64))
  print("Intente de nuevo".center(64))
  print("\n")
  text = "======================================================"
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

def error_datos():
  print("~~~~~~~~~~~~~~~~~~~~~~Gestión hospitalaria~~~~~~~~~~~~~~~~~~~~~~")
  print("\n")
  text = "============Error de datos============"
  centered_text = text.center(64)
  print(centered_text)
  print("\n")
  print("Error: Usuario o contraseña invalida".center(64))
  print("Intente de nuevo".center(64))
  print("\n")
  text = "======================================================"
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