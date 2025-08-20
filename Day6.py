def find_zero_sum_subarrays(arr):
    n = len(arr)
    prefix_sum = 0
    hashmap = {}  # stores prefix_sum -> list of indices
    result = []

    for i in range(n):
        prefix_sum += arr[i]
        if prefix_sum == 0:
            result.append((0, i))
        if prefix_sum in hashmap:
            for start_index in hashmap[prefix_sum]:
                result.append((start_index + 1, i))

        hashmap.setdefault(prefix_sum, []).append(i)

    return result
arr = [1, 2, -3, 3, -1, 2]
print(find_zero_sum_subarrays(arr))
