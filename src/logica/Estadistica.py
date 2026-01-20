class Estadistica:
    def calcular_desviacion_estandar(self, numeros):
    
        if not numeros:
            return 0.0
        
        n = len(numeros)
    
        promedio = sum(numeros) / n
        
        suma_cuadrados = 0
        for x in numeros:
            suma_cuadrados += (x - promedio) ** 2
            
        varianza = suma_cuadrados / n
        return varianza ** 0.5