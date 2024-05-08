import re
class AnaPython:
    @staticmethod
    def countVar(codigo: str) -> str:
        patronDef = r"def\s+[^\(]+\(([^),]+).*\)\s*->\s*\S+\s*:"
        resultado = re.findall(patronDef, codigo)

        variables = []
        for elemento in resultado:
            variable = elemento.split(':')[0]
            variables.append(variable)
            if elemento == "self":
                variables.remove(elemento)

        
        patronDef = r"def\s+[^\(]+\(([^),]+).*\)\s*->\s*\S+\s*:"
        resultado = re.findall(patronDef, codigo)
        

        return variables
    
    def countDef(codigo: str) -> str:
        patron = r"def.+:"
        resultado = re.findall(patron, codigo)
        return resultado
    
def main():
    archivo = open("regExample.py")
    codigo = archivo.read()
    print(f"Funciones: {AnaPython.countDef(codigo)}\nvariables: {AnaPython.countVar(codigo)}")




if __name__ == "__main__":
    main()