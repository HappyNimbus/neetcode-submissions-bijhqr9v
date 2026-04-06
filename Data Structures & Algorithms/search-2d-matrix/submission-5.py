class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = 0
        r = (ROWS * COLS) - 1


        while l <= r:

            m = (l + r)//2

            #get coords
            m_row = m // COLS
            m_col = m % COLS
            value = matrix[m_row][m_col]

            if value == target:
                return True
            
            elif value > target:
                r = m - 1
            else:
                l = m + 1
        
        return False


        

