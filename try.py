nums = [1, 2, 3, 4]

left_product=[1]

for i in range(1,len(nums)):
    left_product.append(left_product[i-1]*nums[i-1])

right_product = [1] * len(nums)
for i in range(len(nums)-2, -1, -1):
    right_product[i] = right_product[i+1]*nums[i+1]

answer = [1] * len(nums)
for i in range(len(nums)):
    answer[i] = left_product[i]*right_product[i]
print(answer)
print(left_product)
print(right_product)