"""
单链表学习程序
重点程序
"""


# 创建结点类
class Node(object):
    def __init__(self, val, next=None):
        self.val = val  # 有用数据
        self.next = next


# 链表的操作
class LinkList(object):
    def __init__(self):
        self.head = Node(None)  # 链表的开头

    def init_list(self, data):
        p = self.head  # 可移动变量ｐ

        for i in data:
            p.next = Node(i)
            p = p.next

    def show(self):
        p = self.head.next

        while p != None:
            print(p.val, end=' ')
            p = p.next
        print()

    # 　尾部插入新的结点
    def append(self, item):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(item)

    #  获取链表长度
    def get_length(self):
        n = 0
        p = self.head
        while p.next is not None:
            n += 1
            p = p.next
        return n

    # 　判断链表是否为空
    def is_empty(self):
        if self.get_length() == 0:
            return True
        else:
            return False

    # 清空链表
    def clear(self):
        self.head.next = None

    # 　获取索引值
    def get_item(self, index):
        p = self.head.next
        i = 0
        #　没有到对应索引号并且遍历索引没有到最后就循环
        while i < index and p is not None:
            i += 1
            p = p.next
        # 如果因为ｐ到最后了则说明越界
        if p is None:
            raise IndexError("list index out of range")
        # ｉ 不小于　ｉｎｄｅｘ说明找到索引结点了
        else:
            return p.val

    def insert(self,index,item):
        if index < 0 or index > self.get_length():
            raise IndexError("list index out of range")

        #　让ｐ移动到待插入位置的前一个
        p = self.head
        i = 0
        while i < index:
            p = p.next
            i += 1

        node = Node(item)  #　创建新的结点
        node.next = p.next  #　插入结点
        p.next = node

    def delete(self,item):
        p = self.head
        while p.next is not None:
            #　如果值相等则越过中间的结点
            if p.next.val == item:
                p.next = p.next.next
                break
            p = p.next
        else:
            print("x not in list")


if __name__ == "__main__":
    # 　创建链表对象
    link = LinkList()

    # 　初始数据
    l = [1, 2, 3, 4, 5]
    link.init_list(l)  # 将初始数据插入链表
    link.show()  # 遍历链表
    link.append(6)  # 尾部插入结点
    link.show()
    print(link.get_length())  # 获取结点个数

    # print(link.is_empty())  # 判断是否为空
    # link.clear()  # 清空链表
    # print(link.is_empty())

    print(link.get_item(4)) #　获取索引值

    link.insert(1,10) # 在某个索引位置插入数据
    link.show()
    link.delete(4)
    link.show()
