class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        coluna = collections.defaultdict(set)
        linha = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in coluna[i] or board[i][j] in linha[j] or board[i][j] in square[(i//3, j//3)]:
                    return False
                coluna[i].add(board[i][j])
                linha[j].add(board[i][j])
                square[i//3,j//3].add(board[i][j])
        return True