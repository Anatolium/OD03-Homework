# Пузырьковая сортировка
array = [5, 7, 4, 3, 8, 2]

def bubble_sort(arr):
    # Количество проходов всегда на единицу меньше количества элементов в массиве
    mas_len = len(arr)
    for run in range(mas_len - 1):
        # Каждый проход приводит к тому, что самый большой элемент "всплывает" и оказывается в конце массива
        for i in range(mas_len - 1 - run):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

print(array)
print(bubble_sort(array))
