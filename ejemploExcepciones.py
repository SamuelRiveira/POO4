class EjemploExcepciones:
    def ZeroDivisionError():
        a = 5
        b = 0
        if (a == 0) or (b == 0):
            raise ZeroDivisionError
        return a / b

    def ValueError():    
        numEntero = "Hola"
        if type(numEntero) != int:
            raise ValueError
        return numEntero

    def FileNotFoundError():
        with open('archivo_que_no_existe.txt', 'r') as f:
            contenido = f.read()
            if f.read():
                raise FileNotFoundError
            return contenido

    def TypeError():
        a = "7"
        b = 4
        if type(a) != int or type(b) != int:
            raise TypeError
        return a + b

    def PermissionError():
        with open('mi_archivo.txt', 'r') as archivo:
            contenido = archivo.read()
            if archivo.read():
                raise PermissionError
            return contenido

    def IndexError():
        pass

    def KeyboardInterrupt():
        pass

    def UnicodeDecodeError():
        pass

    def AttributeError():
        pass

"""#ZeroDivisionError
ejemplo = EjemploExcepciones.ZeroDivisionError()
print(ejemplo)"""

"""#ValueError
ejemplo = EjemploExcepciones.ValueError()
print(ejemplo)"""

"""#FileNotFoundError
ejemplo = EjemploExcepciones.FileNotFoundError()
print(ejemplo)"""

"""#TypeError
ejemplo = EjemploExcepciones.TypeError()
print(ejemplo)"""

#PermissionError
ejemplo = EjemploExcepciones.PermissionError()
print(ejemplo)

#IndexError
ejemplo = EjemploExcepciones.IndexError()
print(ejemplo)

#KeyboardInterrupt
ejemplo = EjemploExcepciones.KeyboardInterrupt()
print(ejemplo)

#UnicodeDecodeError
ejemplo = EjemploExcepciones.UnicodeDecodeError()
print(ejemplo)

#AttributeError
ejemplo = EjemploExcepciones.AttributeError()
print(ejemplo)