"""
辞書リストで指定された単語（許可された単語）を使用して、`start` 単語から `end` 単語までの最短変換シーケンスの長さを計算する関数を作成してください。

各変換ステップでは、必ず1文字だけを変更しなければなりません。すべての中間単語は、文中に存在していなければなりません。

関数は以下のことを行う必要があります。
- 最短のラダーに含まれる単語の総数（`start`と`end`を含む）を返します。
変換シーケンスが不可能な場合は0を返します。
"""

def word_ladder(start: str, end: str, sentence: list[str]) -> int:


if __name__ == "__main__":
    print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5)
    print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0)
