import math

def get_numbers_input() -> list[str]:
    """
    getting from terminal data and returning it
    :return: List of three strings separated by spaces
    """
    return input("Enter list of three digits by space: ").split()


def valid_data(user_input: list[str]) -> list[int]:
    """
    Validate input data and convert to list of integers
    :param user_input: list of three strings
    :return: list of three validated integers ready for work
    """
    if len(user_input) != 3:
        raise ValueError("НАДО 3 ЧИСЛА")

    try:
        return [int(el) for el in user_input]
    except ValueError:
        raise ValueError("ЭТО НЕ ЦЕЛЫЕ ЧИСЛА, ВВЕДИ ЧИСЛА!!")


def roots_of_equation(valid_user_data: list[int]) -> tuple[float,float]:
    """
    finding discriminant and roots by formuls
    :param valid_user_data: list of three integers [a, b, c]
    :return: tuple of two roots
    """
    a, b, c = valid_user_data
    if a == 0:
        raise ValueError("НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ, ТЫЧО")

    d = b**2 - 4*a*c
    if d < 0:
        raise ValueError("ДИСКРИМИНАНТ ОТРИЦАТЕЛЬНЫЙ, УРАВНЕНИЕ НЕ ИМЕЕТ ДЕЙСТВИТЕЛЬНЫХ КОРНЕЙ!")

    x_1 = (-b + math.sqrt(d) ) / (2*a)
    x_2 = (-b - math.sqrt(d)) / (2*a)

    return(x_1, x_2)


def main():
    user_input = get_numbers_input()
    valid_user_data = valid_data(user_input)
    result = roots_of_equation(valid_user_data)
    print("КОРЕШКИ:", result)


if __name__ == '__main__':
    main()