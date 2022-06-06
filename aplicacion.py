def agregar():
    print("--Agregar Datos del producto--")
    codigo = str(input("Codigo: "))
    nombre = str(input("Nombre: "))
    precio = str(input("Precio: "))
    producto = open('codigo.txt','a')
    producto1 = open('nombre.txt','a')
    producto2 = open('precio.txt','a')
    producto.write("\n"+codigo)
    producto1.write("\n"+nombre)
    producto2.write("\n"+precio)
    
    producto.close()
    producto1.close()
    producto2.close()


def salir():
    print("Proceso terminado...")

def leer_archivo(nombre):
    archivo = open(nombre,"rt", encoding=('utf8'))
    contenido = archivo.read()
    return contenido

def listar():
    archivo = open('codigo.txt')
    archivo1=open('nombre.txt')
    archivo2=open('precio.txt')
    for i in range(20):
        print(archivo.readline().strip()+" "+archivo1.readline().strip()+" "+archivo2.readline().strip())
    archivo.close()
    archivo1.close()
    archivo2.close()


def menu():
    print("Datos Producto")
    print("1. Listar")
    print("2. Agregar")
    print("3. Salir")

veces=0
while True:    
    usu=str(input("usuario: "))
    cont=int(input("pass: "))
    if usu==str(leer_archivo('usuario.txt').strip()) and cont==int(leer_archivo('claves.txt').strip()):
        break
    veces+=1
    if veces==3:
        print("demasiados intentos")
        break
if veces<3:
    while True :
        menu()
        op=int(input("elija opcion: "))
        if op == 1:
            listar()
        elif op == 2:
            agregar()
        elif op == 3:
            salir()
            break
        else:
            print("incorrecto")