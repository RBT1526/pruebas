import pandas as pd
import os 



def generacion(hoja):
    ingresos = hoja["Invoice Amount USD"].tolist()
    vendedores = hoja["Vendor Name"].tolist()
    mayor = ingresos.index(max(ingresos))
    return vendedores[mayor], ingresos[mayor]

def moneda_mas(hoja):
    moneda = hoja["Invoice Currency"].tolist()
    mxn = moneda.count("MXN")
    usd = moneda.count("USD")
    if mxn > usd:
        return mxn, "MXN"
    else:
        return usd, "USD"
    

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num

def provedores(hoja):
    provedores = hoja["Vendor Name"].tolist()
    repetido = most_frequent(provedores)
    return repetido


def validacion(hoja):
    validacion = hoja["Validation Status"].tolist()
    cuenta = validacion.count("V")
    return cuenta
    
def vendor_site(hoja):
    vendor = hoja["Vendor Site Code"].tolist()
    most_checked = most_frequent(vendor)
    return most_checked


def menu():
    print("""
          
        BIENVENIDO AL MENU DE CONSULTA
          
           SELECCIONA UNA CONSULTA

 1)QUE PROVEEDOR GENERA MAS INGRESOS

 2)QUE MONEDA ES LA MAS USADA 

 3)QUE PROVEEDOR SE REPITE MAS EN LA BASE DE DATOS

 4)CUANTOS ESTAN VALIDADOS
        
 5)QUE CODIGO DE VENDEDOR SE REPITE MAS

 6)SALIR 

                   
""")
def main():
    hoja = pd.read_excel('Excel.xlsx',header=3) 
    while True:
        os.system(clean)
        menu()
        try:
            opcion = int(input("Escribe el numero de tu opcion: "))
            lista_opcion = [1,2,3,4,5,6]
            if opcion in lista_opcion:
                if opcion == 1:
                    os.system(clean)
                    vendedores, dinero = generacion(hoja)
                    print(f"\n \n \n \n EL PROVEDOR QUE GENERA MAS ES {vendedores} Y GENERO {dinero}")
                    print(f"\n \n \n 1)Regresar \n 2)Salir")
                    option = int(input())
                    if option == 2:
                        break
                elif opcion == 2:
                    os.system(clean)
                    moneda, tip_mon = moneda_mas(hoja)
                    print(f"LA MONEDA MAS USADA ES {tip_mon} y se usa {moneda} veces")
                    print(f"\n \n \n 1)Regresar \n 2)Salir")
                    option = int(input())
                    if option == 2:
                        break
                elif opcion == 3:
                    os.system(clean)
                    repetidos = provedores(hoja)
                    print(f"El proveedor mas repetido es {repetidos}")
                    print(f"\n \n \n 1)Regresar \n 2)Salir")
                    option = int(input())
                    if option == 2:
                        break
                elif opcion == 4:
                    os.system(clean)
                    validados = validacion(hoja)
                    print(f"El numero de provedores validados es de {validados}")
                    print(f"\n \n \n 1)Regresar \n 2)Salir")
                    option = int(input())
                    if option == 2:
                        break
                elif opcion == 5:
                    os.system(clean)
                    vendor = vendor_site(hoja)
                    print(f"El codigo de vendedor mas repetido es {vendor}")
                    print(f"\n \n \n 1)Regresar \n 2)Salir")
                    option = int(input())
                    if option == 2:
                        break
                else:
                    os.system(clean)
                    print("Gracias por su consulta")
                    break
        
        except:
            print("Selecciona una opcion valida")
    




if __name__ == "__main__":
    
    if os.name == "posix":
        clean = "clear"
    else:
        clean = "cls"
    main()



