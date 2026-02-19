class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
            
        rows, cols = len(mat), len(mat[0])
        res = []
        cur_row = cur_col = 0
        goingUp = True

        while len(res) < rows * cols:
            res.append(mat[cur_row][cur_col])
            
            if goingUp:
               
                if cur_col == cols - 1: 
                    cur_row += 1
                    goingUp = False
                elif cur_row == 0:    
                    cur_col += 1
                    goingUp = False
                else:
                    cur_row -= 1
                    cur_col += 1
            else:
               
                if cur_row == rows - 1:
                    cur_col += 1
                    goingUp = True
                elif cur_col == 0:     
                    cur_row += 1
                    goingUp = True
                else:
                    cur_row += 1
                    cur_col -= 1
                    
        return res