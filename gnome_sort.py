# Гномья сортировка
array = [38, 27, 43, 3, 58, 9, 82, 10, 68]


def gnome_sort(arr):
    index = 0
    arr_len = len(arr)
    while index < arr_len:
        # Если текущий элемент больше или равен предыдущему, переходим к следующему
        if index == 0 or arr[index] >= arr[index - 1]:
            index += 1
        else:
            # Если текущий элемент меньше предыдущего, меняем их местами и возвращаемся на шаг назад
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr


print(array)
print(gnome_sort(array))
