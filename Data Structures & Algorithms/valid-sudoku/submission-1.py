class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        trans_board = [[] for _ in range(9)]
        square_board = [[] for _ in range(9)]

        i = 0
        j = 0
        column_offset = 0
        for row in board:
            numbers = []
            row_offset = column_offset - 1
            j = 0
            for num in row:
                if j % 3 == 0:
                    row_offset += 1

                if num != '.':
                    numbers.append(num)
                    trans_board[j].append(num)
                    square_board[row_offset].append(num)

                j += 1
            if len(numbers) != len(set(numbers)):
                return False

            i += 1
            if i % 3 == 0:
                column_offset = i

        for row in trans_board:
            if len(row) != len(set(row)):
                return False

        for row in square_board:
            if len(row) != len(set(row)):
                return False
        return True