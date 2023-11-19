#
# @lc app=leetcode.cn id=497 lang=python3
#
# [497] 非重叠矩形中的随机点
#
from typing import List
# @lc code=start
import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects=rects
        degrees=[0]
        for rect in self.rects:
            x1,y1,x2,y2=rect
            degrees.append((x2-x1+1)*(y2-y1+1)+degrees[-1])
        self.degrees=degrees

    def pick(self) -> List[int]:
        p=random.randrange(self.degrees[-1])
        left=0
        right=len(self.degrees)-1
        while left<right:
            mid=(left+right)//2
            x=self.degrees[mid]
            if p<x:
                right=mid
            else:
                left=mid+1
            
        x1,y1,x2,y2=self.rects[left-1]
        a,b=divmod(p-self.degrees[left-1],y2-y1+1)
        return [x1+a,y1+b]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
# @lc code=end

obj=Solution([[-2,-2,1,1],[2,2,4,6]])
print(obj.pick())
print(obj.pick())
print(obj.pick())
print(obj.pick())
print(obj.pick())
print(obj.pick())
print(obj.pick())
print(obj.pick())