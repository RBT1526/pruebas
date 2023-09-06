import pandas as pd
import os 



def generacion(hoja):
    ingresos = hoja["COSAS 3"].tolist()
    vendedores = hoja["COSAS 4"].tolist()
    mayor = ingresos.index(max(ingresos))
    return vendedores[mayor], ingresos[mayor]

def menu():
    print("""
          
        BIENVENIDO AL MENU DE CONSULTA
          
           SELECCIONA UNA CONSULTA

 1)QUE PROVEEDOR GENERA MAS INGRESOS

 2)QUE MONEDA ES LA MAS USADA 

 3)QUE PROVEEDOR SE REPITE MAS EN LA BASE DE DATOS

 4)CUANTOS ESTAN VALIDADOS

 5)SALIR 

                   
""")
def main():

    
    os.system(clean)
    hoja = pd.read_excel('Excel.xlsx',header=3)
    print(hoja.columns)
    """
    menu()
    try:
        opcion = int(input("Escribe el numero de tu opcion: "))
        lista_opcion = [1,2,3,4]
        if opcion in lista_opcion:
            if opcion == 1:
                os.system(clean)
                vendedores, dinero = generacion(hoja)
                print(f"\n \n \n \n EL PROVEDOR QUE GENERA MAS ES {vendedores} Y GENERO {dinero}")
            elif opcion == 2:
                os.system()
    
                
    
    except:
        print("Selecciona una opcion valida")
    

    generacion(hoja)
    """

#Quien genera mas
#Que moneda es la mas usada
#que provedor se repite mas
#Cuantos estan validados

#column_headers = list(hoja.columns)
#print(column_headers)

if __name__ == "__main__":
    
    if os.name == "posix":
        clean = "clear"
    else:
        clean = "cls"
    main()







