"""
链式队列
重点代码
"""


# 　队列异常
class QueueError(Exception):
    pass


# 队列结点类
class Node(object):
    def __init__(self, val, next=None):
        self.val = val  # 有用数据
        self.next = next

#　链式队列方法实现
class LQueue:
    def __init__(self):
        self.front = self.rear = Node(None)

    def is_empty(self):
        return self.front.next == self.rear.next

    #　入队
    def enqueue(self,elem):
        self.rear.next = Node(elem)
        self.rear = self.rear.next

    #　出队
    def dequeue(self):
        if self.front == self.rear:
            raise QueueError("Queue is empty")
        self.front = self.front.next
        print(self.rear.val)
        return self.front.val

    #　清空队列
    def clear(self):
        self.front = self.rear


if __name__ == "__main__":
    lq = LQueue()


    lq.enqueue(10)
    print(lq.is_empty())









