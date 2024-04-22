class EjemploExcepciones:
    def zeroDivisionError(self):
        a = 5
        b = 0
        if (a == 0) or (b == 0):
            raise ZeroDivisionError
        return a / b

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
        with open('mi_archivo.txt') as archivo:
            contenido = archivo.read()
            if archivo.read() == PermissionError:
                raise PermissionError
            return contenido

    def indexError(self):
        lista = ["tomate", "lechuga", "cebolla"]
        posicion = 2
        if posicion > len(lista) - 1:
            raise IndexError
        return lista[posicion]

    def keyboardInterrupt(self):
        palabra = input("Enter something (Ctrl+C to exit): ")
        if palabra == KeyboardInterrupt:
            raise KeyboardInterrupt
        return f"palabra: {palabra}"

    def unicodeDecodeError(self):
        with open('hola.exe') as archivo:
            contenido = archivo.read()
            if UnicodeError:
                raise UnicodeError
            return contenido
    def attributeError(self):
        objeto = object()
        if 'atributo_que_no_existe' not in dir(objeto):
            raise AttributeError("El atributo no existe")
        return objeto.atributo_que_no_existe

"""#zeroDivisionError
ejemplo = EjemploExcepciones()
print(ejemplo.zeroDivisionError())"""

"""#valueError
ejemplo = EjemploExcepciones()
print(ejemplo.valueError())"""

"""#fileNotFoundError
ejemplo = EjemploExcepciones()
print(ejemplo.fileNotFoundError())"""

"""#typeError
ejemplo = EjemploExcepciones()
print(ejemplo.typeError())"""

"""#permissionError
ejemplo = EjemploExcepciones()
print(ejemplo.permissionError())"""

"""#indexError
ejemplo = EjemploExcepciones()
print(ejemplo.indexError())"""

"""#keyboardInterrupt
ejemplo = EjemploExcepciones()
print(ejemplo.keyboardInterrupt())"""

"""#unicodeDecodeError
ejemplo = EjemploExcepciones()
print(ejemplo.unicodeDecodeError())"""

#attributeError
ejemplo = EjemploExcepciones()
print(ejemplo.attributeError())