# problem: Given an image represented by an NxN matrix, where each pixel
#          in the image is 4 bytes, write a method to rotate the image by 90
#          degrees. Can you do it in place?

# book idea
def rotate_matrix(matrix):
    # check to make sure matrix is square
    reverse_matrix = reversed(matrix)
    return matrix


print(rotate_matrix([[1,2,3, 4],[4,5,6, 4],[7,8,9, 4], [1, 2, 3, 4]]))
