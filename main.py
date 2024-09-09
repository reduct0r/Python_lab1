import sys
import math

def get_coefficient_from_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Некорректное значение. Попробуйте снова.")

def get_coefficient(arg, prompt):
    try:
        return float(arg)
    except (ValueError, TypeError):
        print(f"Некорректное значение для {prompt} в командной строке.")
        return get_coefficient_from_input(prompt)

def get_coefficients():
    if len(sys.argv) == 4:
        A = get_coefficient(sys.argv[1], "коэффициент A")
        B = get_coefficient(sys.argv[2], "коэффициент B")
        C = get_coefficient(sys.argv[3], "коэффициент C")
    else:
        while True:
            A = get_coefficient_from_input("Введите коэффициент A: ")
            if A != 0:
                break
            print("Коэффициент A не должен быть равен нулю. Попробуйте снова.")
        B = get_coefficient_from_input("Введите коэффициент B: ")
        C = get_coefficient_from_input("Введите коэффициент C: ")

    return A, B, C

def solve_quadratic(A, B, C):
    result = []
    D = B * B - 4 * A * C
    if D == 0.0:
        root = -B / (2.0 * A)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-B + sqD) / (2.0 * A)
        root2 = (-B - sqD) / (2.0 * A)
        result.append(root1)
        result.append(root2)
    return result

def solve_biquadratic(A, B, C):
    quadratic_roots = solve_quadratic(A, B, C)
    biquadratic_roots = set()  # Используем set для исключения дубликатов
    for root in quadratic_roots:
        if root >= 0:
            biquadratic_roots.add(math.sqrt(root))
            biquadratic_roots.add(-math.sqrt(root))
    return list(biquadratic_roots)  # Преобразуем set обратно в список для печати

def main():
    A, B, C = get_coefficients()

    print(f"Коэффициенты: A={A}, B={B}, C={C}")
    print(f"Уравнение: {A}*x^4 + {B}*x^2 + {C} = 0")

    result = solve_biquadratic(A, B, C)
    if len(result) == 0:
        print("Нет корней")
    else:
        result = sorted(result)  # Сортируем результат для наглядного вывода
        print(f"Решение: {', '.join(map(str, result))}")

if __name__ == "__main__":
    main()
