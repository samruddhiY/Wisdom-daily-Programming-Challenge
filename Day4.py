def merge(arr1, arr2, m, n):
    import math
    gap = math.ceil((m + n) / 2)
    while gap > 0:
        i = 0
        j = gap
        
        while j < (m + n):
            # i in arr1, j in arr1
            if i < m and j < m:
                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]

            # i in arr1, j in arr2
            elif i < m and j >= m:
                if arr1[i] > arr2[j - m]:
                    arr1[i], arr2[j - m] = arr2[j - m], arr1[i]

            # i in arr2, j in arr2
            else:
                if arr2[i - m] > arr2[j - m]:
                    arr2[i - m], arr2[j - m] = arr2[j - m], arr2[i - m]

            i += 1
            j += 1

      
        if gap == 1:
            gap = 0
        else:
            gap = math.ceil(gap / 2)
