"""
重複のない会議時間間隔のリストをスケジュールするために必要な会議室の最小数を決定し、会議を会議室に割り当てる関数を作成してください。

各会議は、2つの整数のリスト`[開始時刻、終了時刻]`として表されます。

関数は以下のことを行う必要があります。
会議を開始時刻順に並べ替え、空いている会議室に順番に割り当てます。
- 以下の内容を含む辞書を返します。
  - `"total_rooms"`: 必要な部屋数の整数値。
  - `"schedule"`: 各部屋の予約間隔を含むリストのリスト。
- 入力リストが空の場合は、`{"total_rooms": 0, "schedule": []}` を返します。
"""
import sys

def py_room_scheduler(meetings: list[list[int]]) -> dict[str, Any]:
    if meetings == []:
        return {"total_rooms": 0, "schedule": []}

    meetings.sort()
    room: list[list[list[int]]] = [[]]

    n = 0
    room[n].append(meetings[0])
    for mtg in meetings[1:]:
        if room[-1][-1][1] > mtg[0]:
            room.append([mtg])
            n += 1
        else:
            room[n].append(mtg)
    return {"total_rooms": len(room), "schedule": room}


if __name__ == "__main__":
    print(py_room_scheduler([[0, 30], [5, 10], [15, 20]]) == {"total_rooms": 2, "schedule": [[[0, 30]], [[5, 10], [15, 20]]]})
    print(py_room_scheduler([[15, 20], [0, 30], [5, 10]]) == {"total_rooms": 2, "schedule": [[[0, 30]], [[5, 10], [15, 20]]]})
    print(py_room_scheduler([]) == {"total_rooms": 0, "schedule": []})
