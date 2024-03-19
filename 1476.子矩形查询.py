#
# @lc app=leetcode.cn id=1476 lang=python3
#
# [1476] 子矩形查询
#
from sbw import *
# @lc code=start
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.origin=rectangle
        self.updates=[]

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.updates.append([row1,col1,row2,col2,newValue])


    def getValue(self, row: int, col: int) -> int:
        for r1,c1,r2,c2,val in reversed(self.updates):
            if r1<=row<=r2 and c1<=col<=c2:
                return val
        return self.origin[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
# @lc code=end
obj=SubrectangleQueries([[1,1,1],[2,2,2],[3,3,3]])
assert_test(obj,["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue"],[[[[1,1,1],[2,2,2],[3,3,3]]],[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]],eval_list_str('[null,1,null,100,100,null,20]'))

obj=SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
assert_test(obj,["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"],[[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]],eval_list_str('[null,1,null,5,5,null,10,5]'))
