"""
2次元の文字グリッド内で、指定された単語パターンが8方向（東西南北および斜め）すべてに出現する箇所を検索する関数を作成してください。

手順とコードは以下のとおりです。
- (1, 0) -> "H" (水平右方向)
- (-1, 0) -> "H-" (水平左)
- (0, 1) -> "V" (垂直下方向)
- (0, -1) -> "V-" (垂直上向き)
- (1, 1) -> "D1" (右下斜め)
- (-1, -1) -> "D1-" (左上斜め)
- (-1, 1) -> "D2" (斜め上方向)
- (1, -1) -> "D2-" (左下斜め

関数は以下のことを行う必要があります。
- 文字列のグリッド `grid` とターゲット文字列 `pattern` を取得します。
- 一致した各文字に対して、タプルのリスト `(x, y, direction_code)` を返します。ここで、`x` は最初の文字の列インデックス、`y` は最初の文字の行インデックスです。
- `grid` または `pattern` のいずれかが空の場合、空のリスト `[]` を返します。
"""
import sys

DICRECTION = {
    "H" :  (1, 0),
    "H-" : (-1, 0),
    "V" :  (0, 1),
    "V-" : (0, -1),
    "D1" : (1, 1),
    "D1-" : (-1, -1),
    "D2" : (-1, 1),
    "D2-" : (1, -1)
}

def prism_detector(grid: list[str], pattern: str):
    result = []
    num = len(pattern)
    target = list(pattern)

    def _find(x: int, y: int, d: str) -> None:
        dx, dy = DICRECTION[d]
        temx, temy = x, y
        for i, c in enumerate(target):
            if not (0 <= temy < len(grid) and 0 <= temx < len(grid[temy])):
                return
            if grid[temy][temx] != c:
                return
            if i == num - 1:
                result.append((x, y, d))
            temx += dx
            temy += dy

    for y, line in enumerate(grid):
        for x, _ in enumerate(line):
            for d in DICRECTION.keys():
                _find(x, y, d)
    # print(result)
    # sys.exit(1)
    return result




if __name__ == "__main__":
    print(prism_detector(["CAT", "A..", "T.."], "CAT") == [(0, 0, "H"), (0, 0, "V")])
    print(prism_detector([], "CAT") == [])
