def max_sliding_window(arr,k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range (k,len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
print(max_sliding_window(arr, 3))  

arr2 = [2, 1, 5, 1, 3, 2]
print(max_sliding_window(arr2, 3))
