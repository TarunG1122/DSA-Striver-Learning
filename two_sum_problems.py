#two sum
from zoneinfo import reset_tzpath

arr = [2,6,5,8,11]
target = 14

## brute

# vals = {}
#
# for i in range(len(arr)):
#     if (target - arr[i]) in vals:
#         print(i, vals[target - arr[i]])
#
#     vals[arr[i]] = i


### optimized
arr = [2, 5, 6, 8, 11]
target = 14

l = 0
r = len(arr) - 1

while l < r:
    s = arr[l] + arr[r]

    if s == target:
        print(l, r)
        break
    elif s > target:
        r -= 1
    else:
        l += 1


