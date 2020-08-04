# TIME: O(n^2)
# SPACE: O(1)
def rotate(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            # temp = matrix[j][i]
            # matrix[j][i] = matrix[i][j]
            # matrix[i][j] = temp
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    
test = [[1,2,3], [4,5,6], [7,8,9]]


for i in range(len(test)):
    for j in range(len(test[i])):
        print(test[i][j], end='')
    print()

rotate(test)
print('\n\n')

for i in range(len(test)):
    for j in range(len(test[i])):
        print(test[i][j], end='')
    print()