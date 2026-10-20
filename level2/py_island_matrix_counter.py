"""
文字列「1」と「0」を含む2次元行列を受け取り、島の総数を返す関数 island_matrix_counter(matrix) を作成してください。

島とは、連結した「1」のセルの集まりです。セルは、水平方向（左右）または垂直方向（上下）に直接隣接している場合にのみ連結しているとみなされます。斜めのセルは連結しているとはみなされません。

要件：
- 「1」は土地を表します。
- 「0」は水を表します。
各島はそれぞれ正確に1回ずつ数える。
空の行列（または行のない行列）は0を返す必要があります。
- DFS/BFS探索または行列変異を使用して、各島全体を探索できます。
"""
import sys

def island_matrix_counter(matrix: list[list[str]]) -> int:

    def _deep(x: int, y: int) -> None:
        if not (0 <= y < len(matrix) and 0 <= x < len(matrix[y])):
            return
        if matrix[y][x] == "0":
            return
        matrix[y][x] = "0"
        _deep(x + 1, y)
        _deep(x, y + 1)
        _deep(x - 1, y)
        _deep(x, y - 1)

    count = 0
    for y, line in enumerate(matrix):
        for x, cell in enumerate(line):
            if cell == "1":
                count += 1
                _deep(x, y)

    return count


if __name__ == "__main__":
    print(island_matrix_counter([["1", "1", "1", "1", "0"],
                                 ["1", "1", "1", "0", "0"],
                                 ["1", "1", "1", "1", "0"],
                                 ["0", "0", "0", "0", "0"]]) == 1)
    print(island_matrix_counter([["1", "1", "0", "0", "0"],
                                 ["1", "1", "0", "0", "0"],
                                 ["0", "0", "1", "0", "0"],
                                 ["0", "0", "0", "1", "1"]]) == 3)
    print(island_matrix_counter([]) == 0)
