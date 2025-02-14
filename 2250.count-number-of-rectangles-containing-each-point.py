#
# @lc app=leetcode.cn id=2250 lang=python3
# @lcpr version=30204
#
# [2250] 统计包含每个点的矩形数目
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Seg:
    def __init__(self) -> None:
        self.slots=[0]*101
    
    def add(self,x):
        while x<=100:
            self.slots[x]+=1
            x+=x&-x
    
    def query(self,x):
        ret=0
        while x>0:
            ret+=self.slots[x]
            x-=x&-x
        return ret
    
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        sorted_pidx=sorted(range(len(points)),key=points.__getitem__,reverse=True)
        rectangles.sort(reverse=True)
        seg=Seg()
        rid=0
        ret=[0]*len(points)
        M=len(rectangles)
        for pidx in sorted_pidx:
            x,y=points[pidx]
            while rid<M and rectangles[rid][0]>=x:
                seg.add(rectangles[rid][1])
                rid+=1
            ret[pidx]=rid - seg.query(y-1)
        return ret
# @lc code=end
assert Solution().countRectangles(rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]])==[1,3]
assert Solution().countRectangles(rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]])==[2,1]


#
# @lcpr case=start
# [[1,2],[2,3],[2,5]]\n[[2,1],[1,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[2,2],[3,3]]\n[[1,3],[1,1]]\n
# @lcpr case=end

#

