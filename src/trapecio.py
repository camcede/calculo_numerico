import math

def f(x):
    """Función a integrar"""
    return 3 * x * math.sqrt(x**2 + 1)

def trapecio(f, a, b, n):
    """
    Calcula la integral de f en [a, b] usando el método del trapecio con n subintervalos.

    Args:
        f (function): función a integrar
        a (float): límite inferior
        b (float): límite superior
        n (int): número de subintervalos

    Returns:
        float: aproximación de la integral
    """
    h = (b - a) / n
    acum = 0

    print("\nMetodo del Trapecio")
    print("--------------------------------------------------------------")
    print(f"{'i':^3} | {'xi':^10} | {'f(xi)':^10} | {'Coef':^7} | {'Termino':^10}")
    print("--------------------------------------------------------------")

    for i in range(n + 1):
        x_i = a + i * h
        fx = f(x_i)
        coef = 1 if i == 0 or i == n else 2
        termino = coef * fx
        acum += termino
        print(f"{i:^3} | {x_i:^10.5f} | {fx:^10.5f} | {coef:^7} | {termino:^10.5f}")

    resultado = (h / 2) * acum

    print("--------------------------------------------------------------")
    print(f"Aproximacion final: {resultado:.6f}")

    return resultado

if __name__ == "__main__":
    a = 1
    b = 2
    n = 4

    trapecio(f, a, b, n)