def find_monotonic_subarray_bounds(arr):
    if len(arr) == 0:
        return None

    start = 0
    end = 0
    max_length = 1
    current_length = 1
    increasing = arr[1] > arr[0]
    all_same = True  # Флаг, показывающий, если все элементы массива одинаковы

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            all_same = False
        if (arr[i] > arr[i - 1] and increasing) or (arr[i] < arr[i - 1] and not increasing):
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                end = i - 1
                start = end - max_length + 1
            current_length = 2 if arr[i] == arr[i - 1] else 1
            increasing = arr[i] > arr[i - 1]

    # Проверяем, если последний подотрезок является самым длинным
    if current_length > max_length:
        max_length = current_length
        end = len(arr) - 1
        start = end - max_length + 1

    # Особый случай: если все элементы массива одинаковы
    if all_same:
        start, end = 0, 0

    return start, end


# Примеры
arr1 = [-3, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2]
arr2 = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

result1 = find_monotonic_subarray_bounds(arr1)
result2 = find_monotonic_subarray_bounds(arr2)

print("Вывод для массива 1:", result1)
print("Вывод для массива 2:", result2)
