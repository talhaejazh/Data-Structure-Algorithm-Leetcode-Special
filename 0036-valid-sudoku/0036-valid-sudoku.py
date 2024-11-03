class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row=[set() for x in range(9)]
        # col=[set() for y in range(9)]
        # square=[[set() for x in range(3)] for y in range(3)]
        # print(square)
        # for x in range(9):
        #     for y in range(9):
        #         cell_value = board[x][y]
        #         if cell_value=='.':
        #             continue
        #         if cell_value in row[x] or cell_value in col[y] or cell_value in square[x//3][y//3]:
        #             return False
        #         row[x].add(cell_value)
        #         col[y].add(cell_value)
        #         square[x//3][y//3].add(cell_value)
        #     return True
        
        
        rows = [set() for x in range(9)]
        columns = [set() for x in range(9)]
        squares = [[set() for x in range(3)] for y in range(3)]
        
        for x in range(9):
            for y in range(9):
                cell_value = board[x][y]
                if cell_value == ".":
                    continue
                if cell_value in rows[x] or cell_value in columns[y] or cell_value in squares[x//3][y//3]:
                    return False

                rows[x].add(cell_value)
                columns[y].add(cell_value)
                squares[x//3][y//3].add(cell_value)
        
        return True        
        