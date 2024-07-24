# Пузырьковая сортировка
arr = [5, 7, 4, 3, 8, 2]

def bubble_sort(mas):
    # Количество проходов всегда на единицу меньше количества элементов в массиве
    mas_len = len(mas)
    for run in range(mas_len - 1):
        # Каждый проход приводит к тому, что самый большой элемент "всплывает" и оказывается в конце массива
        for i in range(mas_len - 1 - run):
            if mas[i] > mas[i + 1]:
                mas[i], mas[i + 1] = mas[i + 1], mas[i]
    return mas

print(arr)
print(bubble_sort(arr))
