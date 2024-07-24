# Поразрядная сортировка
array = [170, 45, 1024, 75, 90, 802, 24, 2, 66, 5578]


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Подсчитать количество вхождений каждой цифры в текущем разряде
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Изменить count[i] так, чтобы count[i] содержал позицию этой цифры в output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Построить output массив
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Скопировать output массив в arr, чтобы arr теперь содержал отсортированные числа по текущему разряду
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Найти максимальное число, чтобы узнать количество разрядов
    max1 = max(arr)

    # Выполнить сортировку для каждого разряда
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
