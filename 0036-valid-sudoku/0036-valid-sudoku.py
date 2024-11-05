class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for s in range(9)]
        col=[set()for y in range(9)]
        sqr=[[set()for x in range(3)] for y in range(3)]
        print(sqr)
        for x in range(9):
            for y in range(9):
                cell_val=board[x][y]
                if cell_val=='.':
                    continue
                if cell_val in row[x] or cell_val in col[y] or cell_val in sqr[x//3][y//3]:
                    return False
                row[x].add(cell_val)
                col[y].add(cell_val)
                sqr[x//3][y//3].add(cell_val)
        return True
        
        
        # row=[set() for x in range(9)]
        # col=[set() for y in range(9)]
        # square=[[set() for x in range(3)] for y in range(3)]
        # print(square)
        # for x in range(9):
        #     for y in range(9):
        #         cell_value = board[x][y]
        #         if cell_value=='.':
        #             continue
        #         if cell_value in row[x] or cell_value in col[y] or cell_value in square[x//3][y//3]: #check condition to see duplicate number in any col row, saquare matrix
        #             return False
        #         row[x].add(cell_value)
        #         col[y].add(cell_value)
        #         square[x//3][y//3].add(cell_value)
        # return True
        
