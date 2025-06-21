class Nodo:
  def __init__(self, dato):
    self.dato = dato
    self.izquierda = None
    self.derecha = None
#Se hace un recorrido inOrden
def recorrer(nodo):
  if nodo is None:
    return 
  recorrer(nodo.izquierda)
  print(nodo.dato, end=", ")
  recorrer(nodo.derecha)
  
#Se ingresa los valores de los nodos segun la siguiente lista
#[13,7,15,3,8,14,19,18]
raiz = Nodo(13)
nodo7 = Nodo(7)
nodo15 = Nodo(15)
nodo3 = Nodo(3)
nodo8 = Nodo(8)
nodo14 = Nodo(14)
nodo19 = Nodo(19)
nodo18 = Nodo(18)
#Se le asigna un lugar a cada nodo en el arbol binario
raiz.izquierda = nodo7
raiz.derecha = nodo15

nodo7.izquierda = nodo3
nodo7.derecha = nodo8

nodo15.izquierda = nodo14
nodo15.derecha = nodo19

nodo19.izquierda = nodo18

# se recorre el arbol en forma inOrden y se imprime
print("El arbol binario recorrido inOrden queda: ")
recorrer(raiz)
print("\n")
#--------------------------------------------------------------------------------
#Busqueda de un valor dentro del arbol binario
def buscar(nodo, num):
  if nodo is None:               #si el nodo no esta retorna none
    return None
  elif nodo.dato == num:
    return nodo
  elif num < nodo.dato:
    return buscar(nodo.izquierda, num)
  else:
    return buscar(nodo.derecha, num)

# buscar un valor ingresado
numero=int(input("ingrese un numero a buscar en el arbol binario: "))
resultado = buscar(raiz, numero)
if resultado:
  print(f"El número {numero}, si se encuentra en el arbol binario.")
else:
  print(f"El número {numero}, no se encuentra en el arbol binario.")