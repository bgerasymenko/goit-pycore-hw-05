import re

# Функція-генератор, яка знаходить числа в тексті
def generator_numbers(text):
    # Шукаємо числа, які мають пробіли з обох боків
    numbers = re.findall(r'\s(\d+\.\d+)\s', f' {text} ')

    # Повертаємо числа одне за одним
    for num in numbers:
        yield float(num)

# Функція, яка підсумовує знайдені числа
def sum_profit(text, func):
    total = 0.0
    # Використовуємо генератор для отримання чисел і додаємо їх до суми
    for number in func(text):
        total += number

    # Повертаємо загальну суму
    return total

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)

# Виводимо результат
print(f"Загальний дохід: {total_income}")
