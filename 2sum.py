def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i==j:
                continue
            elif nums[i]+nums[j]==target:
                return i,j
    return None

print(twoSum([3,2,3],6))

