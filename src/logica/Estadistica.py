class Estadistica:
    
    def calcular_media(self, numeros):
        if not numeros:
            return 0.0
        return sum(numeros) / len(numeros)

    def calcular_desviacion_estandar(self, numeros):
        if not numeros:
            return 0.0
        
        # 1. Usamos el método auxiliar para obtener la media
        media = self.calcular_media(numeros)
        n = len(numeros)
        
        # 2. Calculamos la suma de diferencias usando esa media
        suma_cuadrados = 0
        for x in numeros:
            suma_cuadrados += (x - media) ** 2
            
        varianza = suma_cuadrados / n
        return varianza ** 0.5