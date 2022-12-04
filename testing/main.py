from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(board, word, index, i, j, last_i, last_j) -> int:
            len1 = 0
            len2 = 0
            len3 = 0
            len4 = 0
            if index <= len(word) - 1 and board[i][j] == word[index]:
                if i - 1 >= 0 and (i-1 != last_i):  # up
                    len1 = backtrack(board, word, index + 1, i - 1, j, i, j)
                if i + 1 <= len(board) - 1 and (i + 1 != last_i):  # down
                    len2 = backtrack(board, word, index + 1, i + 1, j, i, j)
                if j + 1 <= len(board[i]) - 1 and (j + 1 != last_j):  # right
                    len3 = backtrack(board, word, index + 1, i, j + 1, i, j)
                if j - 1 >= 0 and (j - 1 != last_j):  # left
                    len4 = backtrack(board, word, index + 1, i, j - 1, i, j)
                return 1 + max(len1, len2, len3, len4)
            return 0

        for i in range(len(board)):
            for j in range(len(board[i])):
                lenth = 0
                index = 0
                lenth += backtrack(board, word, index, i, j, -1, -1)
                print(lenth)
                if lenth == len(word):
                    return True

        return False


if __name__ == '__main__':
    test = Solution()
    test.exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB")
