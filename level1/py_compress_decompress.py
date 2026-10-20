"""
Write two functions: `compress` and `decompress`.

`compress(s: str) -> str`:
- Takes a string and compresses consecutive repeated characters by appending the count after the character.
- If a character appears only once consecutively, omit the number '1'.
- If the input string is empty, return an empty string.

`decompress(s: str) -> str`:
- Takes a compressed string and expands it back to its uncompressed form.
- Handles multi-digit counts (e.g., "a12" -> 12 'a's).
- If no count follows a character, it counts as 1.

`compress`と`decompress`という2つの関数を作成してください。

`compress(s: str) -> str`:
- 文字列を受け取り、連続して繰り返される文字の後にその回数を追加することで圧縮します。
文字が連続して一度だけ出現する場合は、数字の「1」を省略します。
入力文字列が空の場合は、空の文字列を返します。

`decompress(s: str) -> str`:
圧縮された文字列を受け取り、それを元の非圧縮形式に展開します。
- 複数桁のカウントを処理します（例：「a12」→「a」が12個）。
文字の後にカウント記号がない場合は、1としてカウントされます。
"""

def compress(s: str) -> str:
    res = []
    i = 0
    while i < len(s):
        c = s[i]
        count = 0
        while i < len(s) and s[i] == c:
            count += 1
            i += 1
        res.append(c + (str(count) if count > 1 else ""))
    return "".join(res)

def decompress(s: str) -> str:
    res = []
    i = 0
    while i < len(s):
        c = s[i]
        i += 1
        num = ""
        while i < len(s) and s[i].isdigit():
            num += s[i]  # 数字取得
            i += 1
        res.append(c * (int(num) if num else 1))  #
    return "".join(res)

if __name__ == "__main__":
    print(compress("aabcccccaaa") == "a2bc5a3")
    print(decompress("a2bc5a3") == "aabcccccaaa")
    print(compress("") == "")
