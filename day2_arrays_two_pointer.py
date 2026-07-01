def two_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return f"Found: {arr[left]} + {arr[right]} = {target}"
        elif current_sum > target:
            right -= 1
        else:
            left += 1

    return "no pair found"
    
arr = [1,2,3,4,6,8,9]


print(two_sum(arr, 7)) 
print(two_sum(arr, 11))  
print(two_sum(arr, 20))  