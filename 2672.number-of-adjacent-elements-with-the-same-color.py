#
# @lc app=leetcode.cn id=2672 lang=python3
# @lcpr version=30204
#
# [2672] 有相同颜色的相邻元素数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors=[0]*(n+2)
        ret=[]
        cnt=0
        for idx,color in queries:
            idx+=1
            if color==colors[idx]:
                ret.append(cnt)
                continue
            if colors[idx]!=0:
                cnt-=(colors[idx]==colors[idx-1])+(colors[idx]==colors[idx+1])
            
            colors[idx]=color
            cnt+=(colors[idx]==colors[idx+1])+(colors[idx]==colors[idx-1])
            ret.append(cnt)
        return ret
# @lc code=end
assert Solution().colorTheArray(17,[[11,3],[5,1],[16,2],[4,4],[5,1],[13,2],[15,1],[15,3],[8,1],[14,4],[1,3],[6,2],[8,2],[2,2],[3,4],[7,1],[10,2],[14,3],[6,5],[3,5],[5,5],[9,2],[2,3],[3,3],[4,1],[12,1],[0,4],[16,4],[8,1],[14,3],[15,3],[12,1],[11,5],[3,1],[2,4],[10,1],[14,5],[15,5],[5,2],[8,1],[6,5],[10,2]])==[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,1,2,4,5,6,6,6,6,6,6,6,6,6,6,6,5,4,3,4,3,3,3,4]
assert Solution().colorTheArray(4,[[0,2],[1,2],[3,1],[1,1],[2,1]])==[0,1,1,0,2]


#
# @lcpr case=start
# 4\n[[0,2],[1,2],[3,1],[1,1],[2,1]]\n
# @lcpr case=end

# @lcpr case=start
# 1\n[[0,100000]]\n
# @lcpr case=end

#

