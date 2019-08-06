"""
    逻辑处理模块
    1.0 将核心算法粘贴进来
"""

class GameCoreController:
    """
        游戏核心控制器
    """

    def zero_to_end(list_target):
        for i in range(len(list_target) - 1, -1, -1):
            if list_target[i] == 0:
                del list_target[i]
                list_target.append(0)

    def merge(list_target):
        zero_to_end(list_target)
        for i in range(len(list_target) - 1):
            if list_target[i] == list_target[i + 1]:
                list_target[i] += list_target[i + 1]
                list_target[i + 1] = 0
        zero_to_end(list_target)

    def move_left(map):
        for r in range(len(map)):
            merge(map[r])

    def move_right(map):
        for r in range(len(map)):
            list_merge = map[r][::-1]
            merge(list_merge)
            map[r][::-1] = list_merge

    def move_up(map):
        for c in range(4):
            list_merge = []
            for r in range(4):
                list_merge.append(map[r][c])
            merge(list_merge)
            for r in range(4):
                map[r][c] = list_merge[r]

    def move_down(map):
        for c in range(4):
            list_merge = []
            for r in range(3, -1, -1):
                list_merge.append(map[r][c])
            merge(list_merge)
            for r in range(3, -1, -1):
                map[r][c] = list_merge[3 - r]
