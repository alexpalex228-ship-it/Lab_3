import math
from abc import ABC, abstractmethod


# =====================================================================
# СРЕДНЯЯ СЛОЖНОСТЬ: Задание 2 — Класс «Студент» с выводом информации
# СРЕДНЯЯ СЛОЖНОСТЬ: Задание 7 — Перегрузка оператора +
# =====================================================================
class Student:
    """Класс, представляющий студента."""

    def __init__(self, name: str, group: str, avg_score: float) -> None:
        self.name = name
        self.group = group
        self.avg_score = avg_score

    def display_info(self) -> str:
        """Возвращает форматированную информацию о студенте."""
        return (
            f"Студент: {self.name} | "
            f"Группа: {self.group} | "
            f"Средний балл: {self.avg_score:.2f}"
        )

    def __add__(self, other: "Student") -> str:
        """Перегрузка оператора + (объединение студентов в проектную группу)."""
        if not isinstance(other, Student):
            return NotImplemented
        mean_score = (self.avg_score + other.avg_score) / 2
        return (
            f"Проектная команда: {self.name} и {other.name} "
            f"(общий средний балл: {mean_score:.2f})"
        )


# =====================================================================
# СРЕДНЯЯ СЛОЖНОСТЬ: Задание 4 — Класс «Фигура» (площадь, периметр)
# =====================================================================
class Shape(ABC):
    """Базовый абстрактный класс геометрической фигуры."""

    @abstractmethod
    def area(self) -> float:
        """Вычисляет площадь фигуры."""

    @abstractmethod
    def perimeter(self) -> float:
        """Вычисляет периметр фигуры."""


class Rectangle(Shape):
    """Класс Прямоугольник."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Класс Круг."""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


# =====================================================================
# ПОВЫШЕННАЯ СЛОЖНОСТЬ: Задание 2 — Реализовать паттерн Factory
# =====================================================================
class ShapeFactory:
    """Фабрика для создания геометрических фигур."""

    @staticmethod
    def create_shape(shape_type: str, *args: float) -> Shape:
        """Создает и возвращает объект фигуры по строковому типу."""
        shape_type = shape_type.lower()
        if shape_type == "rectangle":
            if len(args) != 2:
                raise ValueError("Для прямоугольника нужны 2 параметра: ширина и высота.")
            return Rectangle(args[0], args[1])
        if shape_type == "circle":
            if len(args) != 1:
                raise ValueError("Для круга нужен 1 параметр: радиус.")
            return Circle(args[0])
        raise ValueError(f"Неизвестный тип фигуры: {shape_type}")


# =====================================================================
# ПОВЫШЕННАЯ СЛОЖНОСТЬ: Задание 6 — Наследование от встроенного списка
# =====================================================================
class ExtendedList(list):
    """Расширенный список с дополнительными аналитическими методами."""

    def average(self) -> float:
        """Возвращает среднее арифметическое элементов списка."""
        if not self:
            return 0.0
        return sum(self) / len(self)

    def unique_elements(self) -> "ExtendedList":
        """Возвращает новый список только с уникальными элементами (сохраняя порядок)."""
        seen = set()
        result = ExtendedList()
        for item in self:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    def filter_positive(self) -> "ExtendedList":
        """Возвращает список только из положительных чисел."""
        return ExtendedList(x for x in self if isinstance(x, (int, float)) and x > 0)