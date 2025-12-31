'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''

def spiralOrder(matrix):
    value = []
    while matrix:

        # add first row of matrix
        value += matrix.pop(0)

        # add last element of each row
        if matrix and matrix[0]:
            for i in matrix:
                value.append(i.pop())
        
        # add last row of matrix in reverse order
        if matrix:
            value += matrix.pop()[::-1]

        # add first element of all rows in reverse
        if matrix and matrix[0]:
            for i in matrix[::-1]:
                value.append(i.pop(0))
    return value

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))