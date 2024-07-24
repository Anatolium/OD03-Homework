# Сортировка слиянием.
# Исходный массив делится на две половины рекурсивно, пока каждая часть не станет массивом из одного элемента.
# Части массива сливаются в один отсортированный массив путём последовательного сравнения элементов двух массивов
# и добавления меньшего элемента в результирующий массив

array = [38, 27, 43, 3, 58, 9, 82, 10, 68]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Разделение массива на две части
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Слияние двух отсортированных частей
    return merge(left_half, right_half)


def merge(left, right):
    sorted_array = []
    left_index, right_index = 0, 0

    # Слияние до тех пор, пока есть элементы в обоих массивах
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    # Добавление оставшихся элементов
    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])

    return sorted_array


print(array)
print(merge_sort(array))
