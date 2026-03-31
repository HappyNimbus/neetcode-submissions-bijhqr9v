class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        curr_row = 0
        curr_col = len(matrix[curr_row])-1
        rows = len(matrix)
        flag = False
         

        while curr_row < rows and not flag:
            right_val = matrix[curr_row][curr_col]
            
            if right_val < target:
                curr_row += 1
            else:
                flag = True

        if curr_row == rows:
            return False
            
        l = 0
        r = len(matrix[curr_row]) - 1

        while l <= r:

            mid = (l + r) // 2
            mid_val = matrix[curr_row][mid]

            if mid_val == target:
                return True
            elif mid_val > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False

        
        

