#coding=utf-8

class Solution:
    def isValidSudoku(self, board) -> bool:
        rowLen = len(board)
        colLen = len(board[0])
        for row in range(rowLen):
            for col in range(rowLen):
                if board[row][col] == '.':
                    board[row][col] = 0
        print(board)
        for row in range(rowLen):
            for col in range(rowLen):
                # row check
                    for tmp in range(colLen): 
                        if board[row][tmp] !=0 and tmp != col and board[row][tmp] == board[row][col]:
                            return False
                # column check
                    for tmp2 in range(rowLen): 
                        if board[tmp2][col] !=0 and tmp2 != row and board[tmp2][col] == board[row][col]:
                            return False
                # cell  check
                    cellrowStart = row // 3 * 3
                    cellcolStart = col // 3 * 3
                    for i in range(cellrowStart,cellrowStart+3):
                        for j in range(cellcolStart,cellcolStart+3):
                            if(board[i][j] !=0 and board[i][j] == board[row][col] and row!=i and col!=j):
                                return False
        return True

    def isValidSudoku2(self, board):
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += [(c,j),(i,c),(i/3,j/3,c)]
                    print("seen=\n",seen ,end='\n')
        return len(seen) == len(set(seen))

if __name__ == '__main__':
    s = Solution()
    test = [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    print(s.isValidSudoku2(test))