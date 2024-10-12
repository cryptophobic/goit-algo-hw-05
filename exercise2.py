def binary_search(arr, x) -> tuple:
    low = 0
    high = len(arr) - 1
    iterations = 0
    result = None

    while low <= high:
        iterations += 1
        mid = (high + low) // 2
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            result = arr[mid]
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return iterations, x

    # якщо елемент не знайдений
    return  iterations, result


arr = [2.4, 3.5, 4.1, 10.03, 40.1]
x = 10
result = binary_search(arr, x)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
