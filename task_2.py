def binary_search_with_upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] >= target:
            upper_bound = arr[mid]
            right = mid - 1
        else:
            left = mid + 1

    return iterations, upper_bound


if __name__ == "__main__":
    arr = sorted([0.1, 0.5, 1.2, 2.3, 3.4, 5.5, 6.8])
    target = 3.0
    print(binary_search_with_upper_bound(arr, target))
