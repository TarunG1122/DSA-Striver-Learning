# insertion sort


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        current = arr[i]  # element to insert
        j = i - 1

        # shift elements greater than current
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current  # place current in correct position

    return arr


# Example
arr = [5, 3, 8, 4, 2]
print(insertion_sort(arr))

