class Estadistica:
    def calcular_desviacion_estandar(self, numeros):
        if not numeros:
            return 0.0
        
        if len(numeros) == 1:
            return 0.0
            
        return None