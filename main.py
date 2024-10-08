def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    for elem in numbers:
        for item in elem:
            if isinstance(item, (int, float)):
                result += item
            else:
                incorrect_data += 1
                print(f'Некоректный тип данных для подсчета суммы - {item}')
    return result, incorrect_data


def calculate_average(*numbers):
    try:
        summa, incorrect_data = personal_sum(numbers)
        count = sum(
            1 for num in numbers for item in num if isinstance(item, (int, float)))
        try:
            avr = summa / count if count > 0 else 0
            return avr
        except ZeroDivisionError:
            return 0
    except TypeError:
        print('в numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
