import sys
import math

class QuadraticEquation:
    def __init__(self, A=None, B=None, C=None):
        if A is not None and B is not None and C is not None:
            self.A = A
            self.B = B
            self.C = C
        else:
            self.A, self.B, self.C = self.get_coefficients()

    def get_coefficient_from_input(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Некорректное значение. Попробуйте снова.")

    def get_coefficient(self, arg, prompt):
        try:
            value = float(arg)
            if value == 0 and prompt == 'A':
                raise ValueError("Коэффициент A не должен быть равен нулю.")
            return value
        except (ValueError, TypeError):
            print(f"Некорректное значение для {prompt} в командной строке.")
            return self.get_coefficient_from_input(prompt)

    def get_coefficients(self):
        if len(sys.argv) == 4:
            A = self.get_coefficient(sys.argv[1], "A")
            while A == 0:
                print("Коэффициент A не должен быть равен нулю. Попробуйте снова.")
                A = self.get_coefficient_from_input("Введите коэффициент A: ")
            B = self.get_coefficient(sys.argv[2], "B")
            C = self.get_coefficient(sys.argv[3], "C")
        else:
            while True:
                A = self.get_coefficient_from_input("Введите коэффициент A: ")
                if A != 0:
                    break
                print("Коэффициент A не должен быть равен нулю. Попробуйте снова.")
            B = self.get_coefficient_from_input("Введите коэффициент B: ")
            C = self.get_coefficient_from_input("Введите коэффициент C: ")

        return A, B, C

    def get_roots(self):
        A, B, C = self.A, self.B, self.C
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

    def solve_and_print(self):
        print(f"Коэффициенты: A={self.A}, B={self.B}, C={self.C}")
        print(f"Уравнение: {self.A}*x^2 + {self.B}*x + {self.C} = 0")

        result = self.get_roots()
        if len(result) == 1:
            print(f"Корень: {result[0]}")
        elif len(result) == 2:
            print(f"Корни: {result[0]}, {result[1]}")
        else:
            print("Нет корней")

def main():
    equation = QuadraticEquation()
    equation.solve_and_print()

if __name__ == "__main__":
    main()