k = 100
arr = [10, 5, 2, 6, 7]
n = len(arr)

i = j = 0   
ans, p = 0, 1

while j < n:
    p *= arr[j]

    while p >= k and i <= j:
        p //= arr[i]
        i += 1

    ans += j - i + 1
    j += 1

print(ans)