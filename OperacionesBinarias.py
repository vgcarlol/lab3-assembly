
class app():
    def __init__(self):    
        print("Bienvenido al programa creado por Brandon Morales y Carlos Valladares.")
        print("El programa realiza conversiones de binario y hexadecimal a números decimales y viceversa.")
        print("Para proceder, por favor ingrese la opción que deseaa realizar:")
        op = int(input("Selecciones la opción: \n (1) Binario a Decimal \n (2) Hexadecimal a Decimal \n (3) Decimal a Hexadecimal \n (4) Salir \n ->"))

        while(op != 4):   

            if(op == 1):
                n = int(input("Ingrese un decinal de 7 bits rango(0-127): \n -> "))
                print(n)
                if(n>=-127 and n<=127):
                    rev = self.Numero_ABinario(n,n)
                    print("------------------------- \n Decimal ingresado")
                    print(n)
                    print("Binario:")
                    print(rev)
                    rev1 = self.Binario_AComplemeto1(rev)
                    print("Complemento A1")
                    print(rev1)
                    rev2 = self.Binario_AComplemento2(rev1)
                    print("Complemento A2")
                    print(rev2)
                else:
                    print("No cumpe con 7 bits debe estar el rango de 0 y 127 par ser de 7 y el singo llega al 8vo bit")
                    

            if(op == 2):
                hexadecimal = input('Ingresa el número hexadecimal a convertir para decimal : ')
                dec = self.hexadecimal_Anumero(hexadecimal)
                print(dec)

            if(op == 3):
                self.decimal_a_hexadecimal()    
                dec = int(input("Escribe un número decimal, yo lo convertiré a hexadecimal: "))
                hex = self.decimal_a_hexadecimal(dec)
                print(f"El decimal {dec} es {hex} en hexadecimal")

            elif():
                print("El dato ingresado es inválido.")
            op = int(input("Selecciones la opción: \n (1) Binario a Decimal \n (2) Hexadecimal a Decimal \n (3) Decimal a Hexadecimal \n (4) Salir \n ->"))

            


    def Binario_AComplemento2(self,listaBinariaA1):
        l = listaBinariaA1
        acu = 1
        for valor in range(len(l)-1,0,-1):
            i = l[valor]
            if(acu == 0):
                if(i == 0):
                    i = i + acu
                    l[valor] = i
                    pass
                if(i == 1):
                    i = i + acu
                    l[valor] = i
                if(i == 2):
                    i = acu
                    acu = 1
                    l[valor] = i
                    pass
            if(acu == 1):
                if(i == 0):
                    i = i + acu
                    acu = 0
                    l[valor] = i
                    pass
                if(i == 1):
                    i = + i + acu
                    acu = 0
                    l[valor] = i
                    pass
                if(i == 2):
                    i = 0 
                    acu = 1
                    l[valor] = i
                    pass

        return l




        

    def Binario_AComplemeto1(self,listaBinaria):
        listaBinaria = listaBinaria
        for i in range(0,len(listaBinaria)):
            dato = listaBinaria[i]
            if(dato == 1):
                listaBinaria[i] = 0
            if(dato == 0):
                listaBinaria[i] = 1
        return listaBinaria

    def Numero_ABinario(self,n,x):
        numero = abs(n)
        listaBinaria = []
        while numero !=0 :
            r = numero % 2
            listaBinaria.append(r)
            numero //= 2


        if(x>=1):
            #positivo
            listaBinaria.append(0)
        if(x<=-1):
            #negativo
            listaBinaria.append(1)
        rev = listaBinaria[::-1]
        print(listaBinaria)

        return rev


    def hexadecimal_Anumero(hexadecimal):       
        # Función que regresa el verdadero valor hexadecimal.
        dec = int(hexadecimal, base=16)
        print('Número comvertido a decimal :', dec)

    # Por ejemplo, si recibe un 15 devuelve f, y si recibe un número menor a 10, devuelve el número sin modificarlo
    def obtener_caracter_hexadecimal(valor):
        # Lo necesitamos como cadena
        valor = str(valor)
        equivalencias = {
            "10": "a",
            "11": "b",
            "12": "c",
            "13": "d",
            "14": "e",
            "15": "f",
        }
        if valor in equivalencias:
            return equivalencias[valor]
        else:
            return valor


    def decimal_a_hexadecimal(dec):
        hex = ""
        while dec > 0:
            residuo = dec % 16
            verdadero_caracter = obtener_caracter_hexadecimal(residuo)
            hex = verdadero_caracter + hex
            dec = int(dec / 16)
        return hex



    def suma(self,a,b):
        pass
        c = a + b
        list2 = ["0","1"]
        for j in range(0,c):
            # impar 1
            # par 0
            if(j % 2 == 0):
                i = 1
            else:
                i = 0
            respuesta = list2[i]


        return respuesta
            
##

app()#.mainloop()