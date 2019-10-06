"""
    数据模型
"""

class DirectionModel:
    """
        方向数据模型
        枚举  常量(命名全部大写)
    """
    # 在整数基础上，添加一个人容易识别的"标签"
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Location:
    """
        位置
    """
    def __init__(self,r,c):
        self.r_index = r
        self.c_index = c
