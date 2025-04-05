def caching_fibonacci():
    # Створюємо пустий словник, де будемо зберігати значення (кеш)
    cache = {}

    # Створюємо внутрішню функцію fibonacci, яка має доступ до cache
    def fibonacci(n):
        # Перевіряємо крайні випадки
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # Якщо значення вже є у кеші, одразу повертаємо його
        if n in cache:
            return cache[n]

        # Якщо значення немає, обчислюємо рекурсивно і зберігаємо у кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        # Повертаємо обчислене значення
        return cache[n]

    # Повертаємо внутрішню функцію fibonacci
    return fibonacci

# Використовуємо функцію
fib = caching_fibonacci()

# Тестуємо роботу функції
print(fib(10))  # Має вивести 55
print(fib(15))  # Має вивести 610
