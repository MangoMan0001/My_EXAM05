"""
有向グラフに少なくとも1つのサイクルが含まれているかどうかを判定する関数を作成してください。

この関数は、隣接リストを表す辞書を受け取ります。辞書のキーは整数のノードID、値は整数の隣接ノードIDのリストです。

関数は以下のことを行う必要があります。
- 有向グラフにサイクルが含まれている場合は True を返します。
グラフが非巡回グラフである場合、または入力グラフ辞書が空の場合は、False を返します。
・複数の接続されていないコンポーネントを含むグラフを正しく処理する。
"""
import sys

def py_graph_cycle_detector(graph: dict[int, list[int]]) -> bool:
    current = set(graph.keys())
    i = 0
    while current:
        if i > len(graph):
            return True

        next_nodes = set()
        for node in current:
            for nxt in graph.get(node, []):
                next_nodes.add(nxt)
        current = next_nodes
        i += 1
    return False


if __name__ == "__main__":
    print(py_graph_cycle_detector({0: [1], 1: [2], 2: [0]}) == True)
    print(py_graph_cycle_detector({0: [1], 1: [2], 2: []})  == False)
    print(py_graph_cycle_detector({})  == False)
