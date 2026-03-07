nums = [2,0,2,1,1,0]
n = len(nums)

c = z = 0
t = n - 1

while c <= t:
    if nums[c] == 0:
        nums[c], nums[z] = nums[z], nums[c]
        c += 1 
        z += 1

    elif nums[c] == 1:
        c += 1

    else:
        nums[c], nums[t] = nums[t], nums[c]
        t -= 1 

print(nums)
