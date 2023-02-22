class app():
    def __init__(self):
        #tk.__init__()
        a = int(input("Ingrese un número: "))
        print("El valor que ingreso es:"+str(a))

        b = int(input("Ingrese un número: "))
        print("El valor que ingreso es:"+str(b))

        j = self.suma(a,b)
        

        print("El resultado es: "+str(j))
    def suma(self,a,b):
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
            


app()#.mainloop()