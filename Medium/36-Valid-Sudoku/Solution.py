class Solution(object):
    def isValidSudoku(self, board):
        
        
        # for row in board:
        #     # for cell in row:
        #         print(row)
        n = 0
        arr = set()
        for row in board:
            n=0   
            for cell in row:
                if cell in row and cell !=".":
                    print(cell)
                    n+=1
             
            print("--")

        print(n)

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]


# strs = ["","b"]
solution = Solution()
result = solution.isValidSudoku(board)
print(result)