class EjemploExcepciones:
    def zeroDivisionError(self, num, den):
        if (num == 0) or (den == 0):
            raise ZeroDivisionError
        return num / den

    def valueError(self):    
        numEntero = 6
        if numEntero != 4:
            raise ValueError
        return numEntero

    def fileNotFoundError(self):
        with open('archivo_que_no_existe.txt', 'r') as f:
            contenido = f.read()
            if not contenido:
                raise FileNotFoundError("PUTA")
            return contenido

    def typeError(self):
        a = "7"
        b = 4
        if type(a) != int or type(b) != int:
            raise TypeError
        return a + b

    def permissionError(self):
        try:
            a = open("mi_archivo.txt", "r")
            a.write("hola")
        except:
            raise PermissionError
    def indexError(self):
        lista = ["tomate", "lechuga", "cebolla"]
        posicion = 3
        if posicion >= len(lista):
            raise IndexError
        return lista[posicion]

    def keyboardInterrupt(self):
        try:
            palabra = input("Escribe aquí: ")
            if palabra != KeyboardInterrupt:
                True
        except:
            raise KeyboardInterrupt

    def unicodeDecodeError(self):
        try:
            b"\x81".decode("utf-8")
        except UnicodeDecodeError as error:
            raise error
    def attributeError(self):
        objeto = object()
        if 'atributo_que_no_existe' not in dir(objeto):
            raise AttributeError("El atributo no existe")
        return objeto.atributo_que_no_existe
