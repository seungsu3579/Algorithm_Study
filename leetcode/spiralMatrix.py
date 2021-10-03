# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        row= len(matrix)
        col= len(matrix[0])
        
        flag = [ [ 0 for j in range(col) ] for i in range(row) ]
        check = False
        answer = list()
        
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        idx = 0
        direct = direction[0]
        cursor_row = 0
        cursor_col = -1
        
        while True:
            
            cursor_row += direct[1]
            cursor_col += direct[0]
            
            if cursor_row >= row or cursor_row < 0 or cursor_col >= col or cursor_col < 0 or flag[cursor_row][cursor_col] == 1:
                
                cursor_row -= direct[1]
                cursor_col -= direct[0]
                idx += 1
                direct = direction[idx%4]
                
                if check:
                    break
                
                check = True
                
                
            else:
                answer.append(matrix[cursor_row][cursor_col])
                flag[cursor_row][cursor_col] = 1
                check = False
        
        return answer
        