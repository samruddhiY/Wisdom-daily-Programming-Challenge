def findLeaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = arr[-1]  # last element is always a leader
    leaders.append(max_from_right)

    # Traverse from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]

    # Reverse to maintain order as in original array
    leaders.reverse()
    return leaders
