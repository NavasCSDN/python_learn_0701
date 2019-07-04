"""
基本排序算法示例
"""


class Sort:
    def __init__(self, list_):
        self.list_ = list_

    def bubble(self):
        # 　外层循环表示比较多少轮
        for i in range(len(self.list_) - 1):
            # 　内层循环表示每轮比较的次数
            for j in range(len(self.list_) - i - 1):
                # 前一个数比后一个数大则交换位置
                if self.list_[j] > self.list_[j + 1]:
                    self.list_[j], self.list_[j + 1] = \
                        self.list_[j + 1], self.list_[j]

    def select(self):
        # 　比较多少轮
        for i in range(len(self.list_) - 1):
            min = i  # 假定i号位置数字最小
            for j in range(i + 1, len(self.list_)):
                if self.list_[min] > self.list_[j]:
                    min = j
            if i != min:
                self.list_[i], self.list_[min] = \
                    self.list_[min], self.list_[i]

    def insert(self):
        for i in range(1, len(self.list_)):
            x = self.list_[i]
            j = i
            while j > 0 and self.list_[j - 1] > x:
                self.list_[j] = self.list_[j - 1]
                j -= 1
            self.list_[j] = x

    # 一轮交换
    def sub_sort(self, low, high):
        key = self.list_[low]  # 基准数字
        while low < high:
            #　后面的数向前甩
            while low < high and self.list_[high] >= key:
                high -= 1
            self.list_[low] = self.list_[high]
            # 　前面的数向后甩
            while low < high and self.list_[low] < key:
                low += 1
            self.list_[high] = self.list_[low]
        self.list_[low] = key
        return low

    # 　快排函数
    def quick(self, low, high):
        # 　low 列表开头元素索引
        # high 列表结尾元素索引
        if low < high:
            key = self.sub_sort(low, high)
            self.quick(low, key - 1)
            self.quick(key + 1, high)


if __name__ == "__main__":
    l = [4, 1, 2, 6, 7, 3, 9, 8,6,2]
    sr = Sort(l)
    # sr.bubble() #　冒泡
    # sr.select() #　选择
    # sr.insert() #　插入
    sr.quick(0, len(l) - 1)
    print(sr.list_)
