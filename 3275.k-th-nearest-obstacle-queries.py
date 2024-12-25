#
# @lc app=leetcode.cn id=3275 lang=python3
# @lcpr version=30204
#
# [3275] 第 K 近障碍物查询
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        heap=[]
        ret=[]
        for x,y in queries:
            dist=abs(x)+abs(y)
            if len(heap)<k:
                heapq.heappush(heap,-dist)
            else:
                heapq.heappushpop(heap,-dist)
            if len(heap)<k:
                ret.append(-1)
            else:
                ret.append(-heap[0])
        return ret
# @lc code=end
assert Solution().resultsArray(queries = [[1,2],[3,4],[2,3],[-3,0]], k = 2)==[-1,7,5,3]


#
# @lcpr case=start
# [[1,2],[3,4],[2,3],[-3,0]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[5,5],[4,4],[3,3]]\n1\n
# @lcpr case=end

#

