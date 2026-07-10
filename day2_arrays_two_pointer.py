def two_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return left+1,right+1
        elif current_sum > target:
            right -= 1
        else:
            left += 1

    return "no pair found"
    
arr = [1,2,3,4,6,8,9]


