BASE = 16


def converts_numbers_by_base(number: int, base: int) -> str:
    number_str = '0123456789ABCDEF'
    if number < base:
        return number_str[number]
    
    return converts_numbers_by_base(number // base, base) + number_str[number % base]


def input_number() -> int:
    try:
        number = int(input('Введите число для перевода в систему счисления:'))
    except ValueError:
        return input_number()
    return number


if __name__ == '__main__':
    
    number = input_number()
    print(f'Результат в системе счисления {BASE} равен:', converts_numbers_by_base(number, BASE))

    print("Проверка с использованием hex():", hex(number))