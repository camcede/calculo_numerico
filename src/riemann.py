import math

def f(x):
    """Función a integrar"""
    return 3 * x * math.sqrt(x**2 + 1)

def suma_riemann(f, a, b, n):
    """
    Calcula la suma de Riemann izquierda de la función f en [a,b] con n subdivisiones.

    Args:
        f (function): función a integrar
        a (float): límite inferior
        b (float): límite superior
        n (int): número de subdivisiones

    Returns:
        float: aproximación de la integral
    """
    h = (b - a) / n
    acum = 0

    print("\nSuma de Riemann")
    print("-------------------------------------------")
    print(f"{'i':^3} | {'xi':^10} | {'f(xi)':^10} | {'area':^10}")
    print("-------------------------------------------")

    for i in range(n):
        x_i = a + i * h
        fx = f(x_i)
        area = fx * h
        acum += area
        print(f"{i:^3} | {x_i:^10.5f} | {fx:^10.5f} | {area:^10.5f}")

    print("-------------------------------------------")
    print(f"Aproximacion: {acum:.6f}")

    return acum

if __name__ == "__main__":
    a = 1
    b = 2
    n = 4

    suma_riemann(f, a, b, n)
