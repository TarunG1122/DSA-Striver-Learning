arr = [1, 2, 3, 1, 1, 1, 1]
k = 3

prefix_sum = {}
current_sum = 0
max_len = 0

for i in range(len(arr)):
    current_sum += arr[i]

    if current_sum == k:
        max_len = i + 1

    if (current_sum - k) in prefix_sum:
        length = i - prefix_sum[current_sum - k]
        max_len = max(max_len, length)

    if current_sum not in prefix_sum:
        prefix_sum[current_sum] = i

print(max_len)