def search(matrix, target):
    
    rows = len(matrix)
    cols = len(matrix[0])

    i = 0
    j = cols - 1

    while i < rows and j >= 0:
        cur_val = matrix[i][j]

        if cur_val == target:
            return True
        elif cur_val > target:
            j -= 1
        else:
            i += 1

    return False

mat = [[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 60]]
target = 13

print(search(mat, target))