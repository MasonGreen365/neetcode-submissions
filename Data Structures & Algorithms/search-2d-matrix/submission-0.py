"""
1. given mxn matrix and target; return true if target inside matrix
    - matrix is SORTED, first int in each row is greater than last of prev.
    -SORTED means BST but we should store index to track our place

"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m, n = len(matrix), len(matrix[0])
        # #l at start, r at end
        # l, r = [0][0], [-1][-1]
        # medRow, medCol = (m // 2), (n // 2)

        # #how to initialize for loop and for what indices?
        # while l < r:
        #     if matrix[medRow][medCol] > target:
        #         r = [medRow][medCol]
        #     elif matrix[medRow][medCol] < target:
        #         l = [medRow][medCol]
        #     else: 
        #         return True
        # return False

        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1

        while l <= r:
            mid = l + (r - l) // 2
            row, col = mid // cols, mid % cols
            print(f"mid:{mid}, row:{row}, col:{col}")
            if target > matrix[row][col]:
                l = mid + 1
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                return True
        return False
                
        
        