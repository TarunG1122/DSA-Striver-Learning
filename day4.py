# insertion sort

#
# def insertion_sort(arr):
#     n = len(arr)
#
#     for i in range(1, n):
#         current = arr[i]  # element to insert
#         j = i - 1
#
#         # shift elements greater than current
#         while j >= 0 and arr[j] > current:
#             arr[j + 1] = arr[j]
#             j -= 1
#
#         arr[j + 1] = current  # place current in correct position
#
#     return arr
#
#
# # Example
# arr = [7, 2, 9, 1, 5]
# print(insertion_sort(arr))
#



# def selection_sort(arr):
#
#     n = len(arr)
#
#     for i in range(n):
#         min_index = i
#
#         for j in range(i+1,n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#
#     return arr
#
#
#
#
#
#
#
# arr = [7, 2, 9, 1, 5]
# print(selection_sort(arr))


# arr = [7, 2, 9, 1, 5]
# n = len(arr)
#
# lowest = arr[0]
#
# for i in range(1,n):
#     if arr[i] < lowest:
#         print(arr[i])
#
#
# n= len(arr)




#
# def bubble_sort(arr):
#     n = len(arr)
#
#     for i in range(n):
#         for j in range( n - i - 1):   # start from 0, shrink range
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#     print(arr)
#
#
# arr = [10, 15, 4, 23, 0]
# bubble_sort(arr)



