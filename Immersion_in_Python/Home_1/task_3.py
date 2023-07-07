# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует. Отдельно сообщить является ли
# треугольник разносторонним, равнобедренным или равносторонним.


EQUIL = "Triangle with sides: {}, {}, {} is equilateral"
ISOSCELES = "Triangle with sides: {}, {}, {} is isosceles"
USUAL = "Triangle with sides: {}, {}, {} is usual"
NOT_EXIST = "Triangle with sides: {}, {}, {} doesn't exist"
NOT_TRIANGLE = "Figure with sides: {}, {}, {} isn't triangle"


def check_triangle(a, b, c):
    if a == 0 or b == 0 or c == 0:
        res = NOT_TRIANGLE.format(a, b, c)
    else:
        if a + b > c and a + c > b and b + c > a:
            if a == b and a == c:
                res = EQUIL.format(a, b, c)
            elif a == b or a == c or b == c:
                res = ISOSCELES.format(a, b, c)
            else:
                res = USUAL.format(a, b, c)
        else:
            res = NOT_EXIST.format(a, b, c)
    print(res)

check_triangle(2, 4, 7)
check_triangle(3, 3, 4)
check_triangle(5, 5, 5)
check_triangle(3, 4, 5)
check_triangle(6, 7, 0)

