import math


class Figure :
    sides_count = 0

    def __init__(self, color, *sides) :
        self.__color = color
        self.__sides = sides

    def get_color(self) :
        return self.__color

    def __is_valid_color(self, r, g, b) :
        self.r = r
        self.g = g
        self.b = b
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255 :
            return True
        else :
            return False

    def set_color(self, r, g, b) :
        if self.__is_valid_color(r, g, b) :
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides) :
        if len(new_sides) != self.sides_count :
            return False
        for side in new_sides :
            if not isinstance(side, int) or side <= 0 :
                return False
        else:
            return True

    def get_sides(self) :
        return self.__sides

    def __len__(self) :
        return sum(self.__sides)

    def set_sides(self, *new_sides) :
        if self.__is_valid_sides(*new_sides) :
            self.__sides = new_sides


class Circle(Figure) :
    sides_count = 1

    def __init__(self, color, *sides) :
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self) :
        return math.pi * self.__radius ** 2


class Triangle(Figure) :
    sides_count = 3

    def __init__(self, color, *sides) :
        super().__init__(color, *sides)

    def get_square(self) :
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cube(Figure) :
    sides_count = 12

    def __init__(self, color, side_length) :
        sides = [side_length] * 12
        super().__init__(color, sides)

    def get_volume(self):
        side_length = self.get_sides()[0]  # Получаем длину стороны
        return side_length[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)

cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:

circle1.set_color(55, 66, 77)  # Изменится

print(circle1.get_color())

cube1.set_color(300, 70, 15)  # Не изменится

print(cube1.get_color())

# Проверка на изменение сторон:

cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится

print(cube1.get_sides())

circle1.set_sides(15)  # Изменится

print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:

print(len(circle1))

# Проверка объёма (куба):

print(cube1.get_volume())
