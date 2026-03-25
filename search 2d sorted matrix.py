def search(matrix, target):
    
    n1 = len(matrix)
    n2 = len(matrix[0])

    i = 0
    j = n2 - 1

    while 0 <= i < n1 and 0 <= j < n2:
        helper = matrix[i][j]

        if helper == target:
            return True
        elif helper > target:
            j -= 1
        else:
            i += 1

    return False

mat = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

print(search(mat, target))