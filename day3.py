# link: https://www.youtube.com/watch?v=69ZCDFy-OUo&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&index=10


# sum of n natural numbers using recusion

## parameterised way


# def parameterised_way(n,sum):
#
#     if n == 0:
#         print(sum)
#         return
#     parameterised_way(n-1,sum+n)
#
# parameterised_way(3,0)



##### functional way

# def functional_way(n):
#
#     if n == 1:
#         return 1
#
#     return n * functional_way(n-1)
#
# print(functional_way(5))


#################################################################################
##############################################################################
### revsese an array using recursion

### normal way
# arr = [1,2,3,4,2]

# l = 0
# r = len(arr) - 1
#
#
# while l < r:
#
#     arr[l],arr[r] = arr[r],arr[l]
#
#     l += 1
#     r -= 1
#
# print(arr)



#### recursive way


#
# def swap(arr,l,r):
#     arr[l], arr[r] = arr[r], arr[l]
#
# def reverse_number_recursion(arr,l,r):
#
#     if l >= r:
#         return arr
#
#     swap(arr,l,r)
#
#     return reverse_number_recursion(arr,l+1,r-1)
#
# arr = [1,2,3,4,2]
# print(reverse_number_recursion(arr,0,len(arr)-1))








####################################################333333

## check if a string is a palindrome


