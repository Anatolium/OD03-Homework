# Поразрядная сортировка.
# Сортирует числа, обрабатывая их поразрядно, от младшего разряда к старшему
array = [170, 45, 1024, 75, 90, 802, 5578, 24, 2, 66]


def counting_sort(arr, exp):
    arr_len = len(arr)
    output = [0] * arr_len
    count = [0] * 10

    # Подсчитаем количество вхождений каждой цифры в текущем разряде
    for i in range(arr_len):
        index = arr[i] // exp
        count[index % 10] += 1

    # Меняем count[i] так, чтобы count[i] содержал позицию этой цифры в output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Строим output массив
    i = arr_len - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Копируем output массив в arr, чтобы arr теперь содержал отсортированные числа по текущему разряду
    for i in range(arr_len):
        arr[i] = output[i]


def radix_sort(arr):
    # Определяем максимальное число, чтобы узнать количество разрядов
    max1 = max(arr)

    # Выполняем сортировку для каждого разряда
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr


print(array)
print(radix_sort(array))
