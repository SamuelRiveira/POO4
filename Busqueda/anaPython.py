import re
class AnaPython:
    @staticmethod
    def countVar(codigo: str) -> str:
        patron = r"def\s+[^\(]+\(([^),]+).*\)\s*->\s*\S+\s*:"
        resultado = re.findall(patron, codigo)

        variables = []
        for elemento in resultado:
            variable = elemento.split(':')[0]
            variables.append(variable)
            if elemento == "self":
                variables.remove(elemento)

        
        patron = r'\b(\w+)\s*(?:=|\+=|-=|\*=|/=|//=|%=)\s*'
        resultado = re.findall(patron, codigo)
        

        return variables, resultado
    
    def countDef(codigo: str) -> str:
        patron = r"def.+:"
        resultado = re.findall(patron, codigo)
        return resultado
    
def main():
    archivo = open("Busqueda/regExample.py")
    codigo = archivo.read()
    print(f"Funciones: {AnaPython.countDef(codigo)}\nvariables: {AnaPython.countVar(codigo)}")




if __name__ == "__main__":
    main()