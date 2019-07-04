"""
顺序队列
重点代码
"""


# 　队列异常
class QueueError(Exception):
    pass


# 完成队列操作
class SQueue:
    def __init__(self):
        self._elems = []  # 使用列表存储队列数据

    def is_empty(self):
        return self._elems == []

    # 　入队
    def enqueue(self, elem):
        self._elems.append(elem)

    # 出队
    def dequeue(self):
        if not self._elems:
            raise QueueError("Queue is empty")
        return self._elems.pop(0)


if __name__ == "__main__":
    sq = SQueue()
    print(sq.is_empty())
    sq.enqueue(10)
    sq.enqueue(20)
    sq.enqueue(30)
    while not sq.is_empty():
        print(sq.dequeue())
