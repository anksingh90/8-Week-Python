# 2 Sum Problem

def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i):
            if nums[j]+nums[i]==target:
                #print(f"We found the target, values : {nums[j]} & {nums[i]}") 
                return nums[j], nums[i]

nums = [2, 7, 11, 15] 
target = 26

print(two_sum(nums,target))

# This is (O(n^2))
# Space complexity is (O(1)) (Constant Space) 

funcs = [lambda x=x: x**2 for x in range(1, 5)]
print([f() for f in funcs])

