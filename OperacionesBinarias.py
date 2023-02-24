
class app():
    def __init__(self):
        op = int(input("Selecciones la opción: \n (1) Binario a número \n (2) Hexadecimal a número \n (3) Salir \n ->"))

        while(op != 3):   

            if(op == 1):
                n = int(input("Ingrese un decinal de 7 bits rango(0-127): \n -> "))
                print(n)
                if(n>=-127 and n<=127):
                    rev = self.Numero_ABinario(n,n)
                    print("------------------------- \n Número ingresado")
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

            elif(op == 2):
                self.hexadecimal_Anumero()
            op = int(input("Selecciones la opción: \n (1) Binario a número \n (2) Hexadecimal a número \n (3) Salir \n ->"))


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


    def hexadecimal_Anumero(self):       
        return ""


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
            
#

app()#.mainloop()