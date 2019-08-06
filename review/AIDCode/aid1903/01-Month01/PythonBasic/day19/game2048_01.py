"""
    2048 核心算法
"""

# 练习１：定义函数，将零元素移动到末尾
# [2,0,2,0] --> [2,2,0,0]
# [0,2,2,0]  --> [2,2,0,0]
# [0,4,2,4]  --> [4,2,4,0]

""" 方案１
def zero_to_end(list_target):
    # １．将传入的列表中非零元素，拷贝到新列表中．
    # [2, 0, 2, 0] --> [2,2] --> [2,2,0,0]
    # [0, 4, 2, 4]  -->[4, 2, 4] -->[4, 2, 4 ,0]
    # 2. 根据为零元素的数量，在新列表中添加零元素
    # [2, 0, 2, 0] --> [2,2]
    new_list = [item for item in list_target if item != 0]
    # [2, 2] --> [2,2,0,0]
    new_list += [0] * list_target.count(0)
    # 3. 将新列表中元素赋值给传入的列表
    list_target[:] = new_list
"""


# 方案2
def zero_to_end(list_target):
    # 从后往前判断，如果零元素，则删除，在末尾追加零元素
    # [2, 0, 2, 0] --> [2, 2]  --> [2, 2,0,0]
    for i in range(len(list_target) - 1, -1, -1):
        if list_target[i] == 0:
            del list_target[i]
            list_target.append(0)


# list01 = [2, 0, 2, 0]
# zero_to_end(list01)
# print(list01)

# 练习２：定义合并函数
# [2,2,0,0] --> [4,0,0,0]
# [2,0,2,0] --> [4,0,0,0]
# [2,0,0,2] --> [4,0,0,0]
# [2,2,2,0] --> [4,2,0,0]

def merge(list_target):
    # [2,0,2,0] --> [2,2,0,0]       [2,2,2,0]
    zero_to_end(list_target)
    # [2,2,0,0] --> [4,0,0,0]       [4,0,2,0]
    for i in range(len(list_target) - 1):
        # 相邻且相同
        if list_target[i] == list_target[i + 1]:
            list_target[i] += list_target[i + 1]
            list_target[i + 1] = 0
    zero_to_end(list_target)  # [4,0,2,0] --> [4,2,0,0]


# list01 = [2,2,2,0]
# merge(list01)
# print(list01)

# 练习３：将二维列表，以表格的格式显示在控制台中　　
list01 = [
    [2, 0, 4, 2],
    [2, 2, 0, 0],
    [2, 0, 4, 4],
    [4, 0, 0, 2],
]


def print_map(map):
    for r in range(len(map)):
        for c in range(len(map[r])):
            print(map[r][c], end=" ")
        print()


# print_map(list01)

# 练习４：定义向左移动函数．１１：５０
"""
    [2,0,0,2]           [4,0,0,0] 
    [2,2,0,0]           [4,0,0,0]
    [2,0,4,4]           [2,8,0,0]
    [4,0,0,2]           [4,2,0,0]
"""


def move_left(map):
    # 获取第行
    for r in range(len(map)):
        # 从左往右获取行
        # 交给merge进行合并
        merge(map[r])


def move_right(map):
    # 获取第行
    for r in range(len(map)):
        # 从右往左获取行
        # 交给merge进行合并
        list_merge = map[r][::-1]
        merge(list_merge)
        map[r][::-1] = list_merge


# 作业１：定义向上移动函数
# 从上往下获取列
# 交给合并方法
# 还给原列
"""
[0][0]
[1][0]
[2][0]
[3][0]
"""


def move_up(map):
    for c in range(4):
        list_merge = []
        #  从上往下获取列  形成一维列表
        for r in range(4):  # 0   1  2    3
            list_merge.append(map[r][c])
        # 交给合并方法
        merge(list_merge)
        # 将合并后的结果list_merge，还原给原二维列表
        for r in range(4):  # 0   1  2    3
            map[r][c] = list_merge[r]


# 作业２：定义向下移动函数  10:45
# 从下往上获取列
# 交给合并方法
# 还给原列
def move_down(map):
    for c in range(4):
        list_merge = []
        #  从上往下获取列  形成一维列表（从左到右）
        for r in range(3, -1, -1):  # 3   2    1   0
            list_merge.append(map[r][c])
        # 交给合并方法
        merge(list_merge)
        # 将合并后的结果list_merge（从左到右），还原给原二维列表
        for r in range(3, -1, -1): # 3 2 1 0
            map[r][c] = list_merge[3 - r]# 0 1 2 3


# move_left(list01)
# move_right(list01)
# move_up(list01)
move_down(list01)
print_map(list01)

"""
    ２０４８游戏
    规则：
        游戏运行，在４＊４的方格中，出现两个随机的数字．
        产生随机数的策略：10%的概率是４，90%的概率是2.
        用户移动方格（wsad）,方格内的数字按照相应规则进行合并．
        如果地图有变化(数字移动／数字合并)，再产生１个随机数．
        游戏结束：数字不能合并，也没有空白位置．
    架构：
            逻辑处理模块     　　　　　　　　　Controller
            界面视图模块(控制台／pygame/.....)View
            数据模型模块..
            程序入口模块
    步骤：
    　　（一）逻辑处理模块 
             创建游戏核心类GameCoreController
             (1)将核心算法粘贴进来16:32
             (2)将所有参数，改为成员变量．16:50
             (3)产生新数字
             　　　-- 计算所有空白位置(为０的位置).
                   -- 随机选择一个位置
                   -- 根据概率产生数字，存入列表的相应位置．
         （二）界面视图模块
         　　　创建游戏核心类对象
         　　　调用核心类对象的生成数字方法
            　　while True:
                  呈现界面
                  获取用户输入，调用核心类对象的移动方法．　
                  产生随机数
        　(三)如果地图有变化(数字移动／数字合并)，再产生１个随机数．
        　(四)游戏结束：数字不能合并，也没有空白位置．
        
"""









