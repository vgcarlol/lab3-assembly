
class app():
    def __init__(self):

        op = int(input("Selecciones la opción: \n (1) Binario a número \n (2) Hexadecimal a número \n ->"))
        if(op == 1):
            n = int(input("Ingrese un decinal de 8 bits "))
            print(n)
            if(n>=-127 and n<=127):
                rev = self.Numero_ABinario(n,n)
                print("Binario:")
                print(rev)
                rev1 = self.Binario_AComplemeto1(rev)
                print("Complemento A1")
                print(rev1)
                rev2 = self.Binario_AComplemeto1()

            else:
                print("No cumpe con 8 bits debe estar el rango de 0 y 127 par ser de 8")

        elif(op == 2):
            self.hexadecimal_Anumero()


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