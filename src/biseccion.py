# Br. Camila Cedeño
# C.I. 30.870.444
import math

def f(x):
    """
    Función a la que se desea hallar la raíz.
    En este caso: f(x) = sen(x) - x²
    Args:
        x (float): valor en el que se evalúa la función.
    Returns:
        float: resultado de la evaluación.
    """
    return math.sin(x) - x**2

def biseccion(f, a, b, er, n):
    """
    Método de Bisección
    Args:
        f (function): función continua a evaluar.
        a (float): límite inferior del intervalo.
        b (float): límite superior del intervalo.
        er (float): error relativo máximo aceptado.
        n (int): número máximo de iteraciones.
    Returns:
        tuple: (raíz aproximada, último error relativo)
    """
    i = 0 # Iteración actual
    ei = 1.0 # Error relativo inicial (100%)
    m_anterior = None # Guardará el valor medio anterior

    # Encabezado de la tabla
    print("\nMetodo de Biseccion")
    print("-------------------------------------------")
    print(f"{'i':^3} | {'m':^10} | {'f(m)':^10} | {'Error':^10}")
    print("-------------------------------------------")

    while ei > er and i < n:
        m = (a + b) / 2 # Punto medio del intervalo
        fm = f(m) # Evaluación de la función en m

        # Cálculo del error relativo si no es la primera iteración
        if m_anterior is not None:
            ei = abs((m - m_anterior) / m)

        # Imprime los valores actuales en la tabla
        print(f"{i:3} | {m:10.5f} | {fm:10.5f} | {ei:10.5f}")

        # Decide en qué subintervalo continuar
        if f(a) * fm < 0:
            b = m
        elif fm * f(b) < 0:
            a = m
        else:
            break # Se encontró la raíz exacta o suficientemente buena

        m_anterior = m
        i += 1

    print("-------------------------------------------")
    print(f"Raiz aproximada: {m:.6f} con error: {ei:.6f}\n")

    return m, ei

# Ejecución principal
if __name__ == "__main__":
    a = 0.5 # Límite inferior
    b = 1.0 # Límite superior
    er = 0.01 # Tolerancia del error relativo
    n = 50 # Máximo número de iteraciones

    # Llamada al método de Bisección
    biseccion(f, a, b, er, n)