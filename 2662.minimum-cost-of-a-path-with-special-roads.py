#
# @lc app=leetcode.cn id=2662 lang=python3
# @lcpr version=30204
#
# [2662] 前往目标的最小代价
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        cache=defaultdict(lambda:float('inf'))
        vis=set()
        cache[tuple(start)]=0
        t=tuple(target)
        while True:
            v,dv=None,-1
            for p,d in cache.items():
                if p not in vis and (dv==-1 or d<dv):
                    v=p
                    dv=d
            
            if v==t: return dv
            vis.add(v)
            vx,vy=v
            cache[t]=min(cache[t],dv+t[0]-vx+t[1]-vy)
            for x1,y1,x2,y2,cost in specialRoads:
                w=(x2,y2)
                cache[w]=min(cache[w],dv+cost+abs(x1-vx)+abs(y1-vy))

# @lc code=end
assert Solution().minimumCost([1,1],[10,8],[[6,4,9,7,1],[5,2,2,1,3],[3,2,5,5,2]])==10
assert Solution().minimumCost(start = [1,1], target = [10,4], specialRoads = [[4,2,1,1,3],[1,2,7,4,4],[10,3,6,1,2],[6,1,1,2,3]])==8
assert Solution().minimumCost(start = [3,2], target = [5,7], specialRoads = [[5,7,3,2,1],[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]])==7
assert Solution().minimumCost(start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]])==5


#
# @lcpr case=start
# [1,1]\n[4,5]\n[[1,2,3,3,2],[3,4,4,5,1]]\n
# @lcpr case=end

# @lcpr case=start
# [3,2]\n[5,7]\n[[5,7,3,2,1],[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n[10,4]\n[[4,2,1,1,3],[1,2,7,4,4],[10,3,6,1,2],[6,1,1,2,3]]\n
# @lcpr case=end

#

