"""
1からn^2までの数値を時計回りの螺旋状に並べたn×nの2次元行列を生成する関数を作成してください。

螺旋は左上のセル（0, 0）から始まり、右、下、左、上へと進み、内側に向かって続きます。
"""


def generate_spiral(n: int) -> list[list[int]]:
    list = []
    i = 0
    j = 0
    while i < n:
        line = []
        j = 0
        while j < n:
            line.append("*")
            j += 1
        list.append(line)
        i += 1
    i = 0
    j = 0
    list[i][j] = 1
    pre = list[i][j]
    while _is_over(list):
        # R
        while  j + 1 < n and list[i][j + 1] == "*":
            j += 1
            list[i][j] = pre + 1
            pre = list[i][j]
        # D
        while i + 1 < n  and list[i + 1][j] == "*":
            i += 1
            list[i][j] = pre + 1
            pre = list[i][j]
        # L
        while 0 <= j - 1 and list[i][j - 1] == "*":
            j -= 1
            list[i][j] = pre + 1
            pre = list[i][j]
        # U
        while 0 <= i - 1 and list[i - 1][j] == "*":
            i -= 1
            list[i][j] = pre + 1
            pre = list[i][j]


    # print(list, _is_over(list))
    # import sys
    # sys.exit(1)
    return list

def _is_over(list: list[list[list[int]]]) -> bool:
    return any("*" in line for line in list)

if __name__ == "__main__":
    print(generate_spiral(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
    print(generate_spiral(4) == [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
    print(generate_spiral(1) == [[1]])
