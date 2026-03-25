# o(nlogn)

nums = [1,5,1,1,6,4]
arr = sorted(nums)

n = len(nums)
mid = (n - 1) // 2
i = mid
j = n - 1

for k in range(0, n):
    if k % 2 == 0:
        nums[k] = arr[i]
        i -= 1
    else:
        nums[k] = arr[j]
        j -= 1

print(nums)

# o(n)
    









