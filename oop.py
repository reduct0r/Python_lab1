import sys
import math

class BiquadSolver:
    def __init__(self):
        self.A = None
        self.B = None
        self.C = None

    def get_coefficient_from_input(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Некорректное значение. Попробуйте снова.")

    def get_coefficient(self, arg, prompt):
        try:
            return float(arg)
        except (ValueError, TypeError):
            print(f"Некорректное значение для {prompt} в командной строке.")
            return self.get_coefficient_from_input(prompt)

    def get_coefficients(self):
        if len(sys.argv) == 4:
            self.A = self.get_coefficient(sys.argv[1], "коэффициент A")
            self.B = self.get_coefficient(sys.argv[2], "коэффициент B")
            self.C = self.get_coefficient(sys.argv[3], "коэффициент C")
        else:
            while True:
                self.A = self.get_coefficient_from_input("Введите коэффициент A: ")
                if self.A != 0:
                    break
                print("Коэффициент A не должен быть равен нулю. Попробуйте снова.")
            self.B = self.get_coefficient_from_input("Введите коэффициент B: ")
            self.C = self.get_coefficient_from_input("Введите коэффициент C: ")

    def solve_quadratic(self, A, B, C):
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

    def solve_biquadratic(self):
        quadratic_roots = self.solve_quadratic(self.A, self.B, self.C)
        biquadratic_roots = set()  # Используем set для исключения дубликатов
        for root in quadratic_roots:
            if root > 0:
                biquadratic_roots.add(math.sqrt(root))
                biquadratic_roots.add(-math.sqrt(root))
            elif root == 0:
                biquadratic_roots.add(math.sqrt(root))
        return list(biquadratic_roots)  # Преобразуем set обратно в список

    def main(self):
        self.get_coefficients()

        print(f"Коэффициенты: A={self.A}, B={self.B}, C={self.C}")
        print(f"Уравнение: {self.A}*x^4 + {self.B}*x^2 + {self.C} = 0")

        result = self.solve_biquadratic()
        if len(result) == 0:
            print("Нет корней")
        else:
            print(f"Решение: {', '.join(map(str, result))}")

if __name__ == "__main__":
    solver = BiquadSolver()
    solver.main()
