### first largest element in an array

# arr = [34,43,5,2,5,64,6,3,9494]
#
# n= len(arr)
#
# largest = arr[0]
# for i in range(1,n):
#     if arr[i] > largest:
#         largest = arr[i]
#
# print(largest)
#
#


#### second largest element


arr = [85,3,5,33,5,4,2,4,5,112]

flar = arr[0]
slar = -1

for i in range(1,len(arr)):
    if arr[i] > flar:
        slar = flar
        flar =arr[i]

    elif arr[i] > slar and arr[i] != flar:
        slar = arr[i]

print(slar)