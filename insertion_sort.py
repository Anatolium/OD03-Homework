# Сортировка вставками
array = [-3, 5, 0, -8, 1, 10]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            print(f"Меняю значение arr[{j + 1}] ({arr[j + 1]}) на значение arr[{j}] ({arr[j]})")
            arr[j + 1] = arr[j]
            print(arr)
            j -= 1
        print(f"Меняю значение arr[{j + 1}] ({arr[j + 1]}) на значение key ({key})")
        arr[j + 1] = key
        print(arr)
    return arr

print(array)
print("Результат:", insertion_sort(array))
