class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        l = 0
        r = (ROWS * COLS) - 1

        while l <= r:

            mid_point = (l + r) // 2

            cord_row = mid_point // COLS #5/4 = 2
            cord_col = mid_point % COLS # 5 % 3 = 2

            if matrix[cord_row][cord_col] == target:
                return True
            elif matrix[cord_row][cord_col] > target:
                r = mid_point - 1
            else:
                l = mid_point + 1
        
        return False


        

