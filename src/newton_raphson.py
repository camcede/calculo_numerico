# Br. Camila Cedeño
# C.I. 30.870.444
import math

def f(x):
    """
    Función a la que se desea hallar la raíz.

    En este caso: f(x) = cos(x) - x

    Args:
        x (float): valor en el que se evalúa la función.

    Returns:
        float: resultado de la evaluación.
    """
    return math.cos(x) - x

def df(x):
    """
    Derivada de la función f.

    En este caso: f'(x) = -sen(x) - 1

    Args:
        x (float): valor en el que se evalúa la derivada.

    Returns:
        float: resultado de la evaluación.
    """
    return -math.sin(x) - 1

def newton_raphson(f, df, x0, er, n):
    """
    Método de Newton-Raphson 

    Args:
        f (function): función a evaluar.
        df (function): derivada de f.
        x0 (float): estimación inicial.
        er (float): error relativo máximo aceptado.
        n (int): número máximo de iteraciones.

    Returns:
        tuple: (raíz aproximada, último error relativo)
    """
    i = 0
    xi = x0
    ei = 1.0

    # Encabezado de la tabla
    print("\nMetodo de Newton-Raphson")
    print("--------------------------------------------------")
    print(f"{'i':^3} | {'xi':^10} | {'xi+1':^10} | {'Error':^10}")
    print("--------------------------------------------------")

    while ei > er and i < n:
        fxi = f(xi)
        dfxi = df(xi)

        if dfxi == 0:
            print("Derivada cero, no se puede continuar.")
            break

        xi1 = xi - fxi/dfxi
        if i > 0:
            ei = abs((xi1 - xi) / xi1)
        else:
            ei = 1.0 # Primer error arbitrario

        print(f"{i:^3} | {xi:^10.6f} | {xi1:^10.6f} | {ei:^10.6f}")

        xi = xi1
        i += 1

    print("--------------------------------------------------")
    print(f"Raiz aproximada: {xi:.6f} con error: {ei:.6f}\n")

    return xi, ei

if __name__ == "__main__":
    x0 = 1.0 # Estimación inicial
    er = 0.0001 # Tolerancia
    n = 20 # Máximo de iteraciones

    newton_raphson(f, df, x0, er, n)