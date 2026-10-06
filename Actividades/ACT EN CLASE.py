
import time

def suma_objetivo(lista, objetivo):
    n = len(lista)
    for i in range(n):
        for j in range(1 + 1, n):
            if lista[1] + lista[j] == objetivo:
                return True
        return False


if __name__ == "__main__":
     lista = [1, 2, 3, 4, 5]

     #Generar lista
     lista = [1 for i in range(10000)]


     objetivo = 9
     resultado = suma_objetivo(lista, objetivo)

     inicio = time.perf_counter()

     final = time.perf_counter()

     print(f"Tiempo de ejecucion: {final - inicio:.6f} segundos")
