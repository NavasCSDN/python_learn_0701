"""
    逻辑处理模块
    1.0 将核心算法粘贴进来
    2.0 将所有参数，改为成员变量．
"""


class GameCoreController:
    """
        游戏核心控制器
    """

    def __init__(self):
        self.__map = [
            [2, 0, 4, 2],
            [2, 2, 0, 0],
            [2, 0, 4, 4],
            [4, 0, 0, 2],
        ]
        self.__list_merge = []

    @property
    def map(self):
        return self.__map

    def zero_to_end(self):
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def merge(self):
        self.zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                self.__list_merge[i + 1] = 0
        self.zero_to_end()

    def move_left(self):
        for r in range(len(self.__map)):
            self.__list_merge[:] = self.__map[r]
            self.merge()
            self.__map[r][:] = self.__list_merge

    def move_right(self):
        for r in range(len(self.__map)):
            self.__list_merge[:] = self.__map[r][::-1]
            self.merge()
            self.__map[r][::-1] = self.__list_merge

    def move_up(self):
        for c in range(4):
            # 清空合并列表，目的：避免之前列表中的结果，对本次有影响．
            self.__list_merge.clear()
            for r in range(4):
                self.__list_merge.append(self.__map[r][c])
            self.merge()
            for r in range(4):
                self.__map[r][c] = self.__list_merge[r]

    def move_down(self):
        for c in range(4):
            self.__list_merge.clear()
            for r in range(3, -1, -1):
                self.__list_merge.append(self.__map[r][c])
            self.merge()
            for r in range(3, -1, -1):
                self.__map[r][c] = self.__list_merge[3 - r]


def print_map(map):
    print("----------------")
    for r in range(len(map)):
        for c in range(len(map[r])):
            print(map[r][c], end=" ")
        print()


if __name__ == "__main__":
    core = GameCoreController()
    print_map(core.map)
    core.move_up()
    print_map(core.map)
    core.move_down()
    print_map(core.map)
    core.move_left()
    print_map(core.map)
    core.move_right()
    print_map(core.map)
