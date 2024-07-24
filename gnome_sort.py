# Гномья сортировка
array = [38, 27, 43, 3, 58, 9, 82, 10, 68]


def gnome_sort(arr):
    index = 0
    n = len(arr)
    while index < n:
        if index == 0 or arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr


print(array)
print(gnome_sort(array))
