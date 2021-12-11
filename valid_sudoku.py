#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
  

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
#         for b in board:
#             temp='.'.join(b)
#             temp=temp.replace('.','')
#             if len(temp)!=len(set(temp)):
#                 return False
#         for i in range(9):
#             temp = ''.join(board[j][i] for j in range(9))
#             temp=temp.replace('.','')
#             if len(temp)!=len(set(temp)):
#                 return False
#         for i in range(3):
#             for j in range(3):
#                 tmp = ''.join(board[3*i+m][3*j+n] for m in range(3) for n in range(3)) ### great
#                 tmp = tmp.replace('.', '')
#                 if len(tmp) != len(set(tmp)):
#                     return False
#         return True
                
            
        row = {i: [] for i in range(9)}
        col = {i: [] for i in range(9)}
        box = {i: [] for i in range(9)}
        
        for i in range(9):
            for j in range(9):
                e = board[i][j]
                box_index = (i // 3) * 3 + j // 3
                
                if e == '.':
                    continue
                    
                if e in row[i] or e in col[j] or e in box[box_index]:
                    return False
                else:
                    row[i].append(e)
                    col[j].append(e)
                    box[box_index].append(e)
                    
        return True
 