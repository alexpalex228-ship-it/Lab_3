from models import ExtendedList, ShapeFactory, Student


def main() -> None:
    print("=== Лабораторная работа № 3. Вариант 2 ===\n")

    # 1. Задание 2 (средняя): Класс «Студент»
    print("--- 1. Класс «Студент» ---")
    student1 = Student("Алексей", "ИВТ-21", 4.75)
    student2 = Student("Мария", "ИВТ-21", 4.95)
    print(student1.display_info())
    print(student2.display_info())

    # 2. Задание 7 (средняя): Перегрузка оператора +
    print("\n--- 2. Перегрузка оператора '+' ---")
    team_info = student1 + student2
    print(team_info)

    # 3. Задание 4 (средняя) и Задание 2 (повышенная): Фигура + Паттерн Factory
    print("\n--- 3. Класс «Фигура» и паттерн «Factory» ---")
    rect = ShapeFactory.create_shape("rectangle", 5.0, 10.0)
    circle = ShapeFactory.create_shape("circle", 7.0)

    print(
        f"Прямоугольник (5x10): Площадь = {rect.area():.2f}, "
        f"Периметр = {rect.perimeter():.2f}"
    )
    print(
        f"Круг (R=7): Площадь = {circle.area():.2f}, "
        f"Периметр = {circle.perimeter():.2f}"
    )

    # 4. Задание 6 (повышенная): Наследование от встроенного списка
    print("\n--- 4. Наследование от встроенного списка (ExtendedList) ---")
    numbers = ExtendedList([10, -5, 20, 10, 30, -2, 20])
    print(f"Исходный список: {numbers}")
    print(f"Среднее значение: {numbers.average():.2f}")
    print(f"Уникальные элементы: {numbers.unique_elements()}")
    print(f"Только положительные: {numbers.filter_positive()}")


if __name__ == "__main__":
    main()