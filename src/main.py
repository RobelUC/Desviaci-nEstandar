import sys
import os

# Truco para que Python encuentre la carpeta src si ejecutamos desde aquí
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.logica.Estadistica import Estadistica

def main():
    print("DESVIACIÓN ESTÁNDAR")
    print("Ingresa los números uno por uno.")
    print("Escribe 'x'  para calcular la desviación.\n")

    numeros = []
    
    while True:
        entrada = input("Ingresa un número: ")
        
        if entrada.lower() in ['x', 'calcular']:
            break
        
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, ingresa un número válido.")

    if numeros:
        estadistica = Estadistica()
        media = estadistica.calcular_media(numeros)
        resultado = estadistica.calcular_desviacion_estandar(numeros)
        
        print("\n----------------RESULTADOS----------------")
        print(f"Números ingresados: {numeros}")
        print(f"Cantidad de datos (N): {len(numeros)}")
        print(f"Desviación Estándar: {resultado:.4f}")
        print(f"Media (Promedio): {media:.4f}")
    else:
        print("No ingresaste ningún número.")

if __name__ == "__main__":
    main()