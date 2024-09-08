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
    if sys.argv[1] == 0:
        print(f"Некорректное значение для {prompt} в командной строке.")
        return get_coefficient_from_input(prompt)
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

def get_roots(A, B, C):
    result = []
    D = B*B - 4*A*C
    if D == 0.0:
        root = -B / (2.0*A)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-B + sqD) / (2.0*A)
        root2 = (-B - sqD) / (2.0*A)
        result.append(root1)
        result.append(root2)
    return result


def main():
    A, B, C = get_coefficients()

    print(f"Коэффициенты: A={A}, B={B}, C={C}")
    print(f"Уравнение: {A}*x^2 + {B}*x + {C} = 0" )
    
    result = get_roots(A, B, C)
    if len(result) == 1:
        print(f"Корень: {result[0]}")
    elif len(result) == 2:
        print(f"Корни: {result[0]}, { result[1]}")
    else:
        print("Нет корней")
        
   
if __name__ == "__main__":
    main()

