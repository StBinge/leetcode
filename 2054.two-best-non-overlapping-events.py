#
# @lc app=leetcode.cn id=2054 lang=python3
# @lcpr version=30204
#
# [2054] 两个最好的不重叠活动
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key= lambda x:x[0])
        heap=[]
        pre_mx=ret=0
        for s,e,v in events:
            while heap and s>heap[0][0]:
                pre_mx=max(pre_mx,heapq.heappop(heap)[1])
            ret=max(ret,v+pre_mx)
            heapq.heappush(heap,[e,v])
        return ret


# @lc code=end
assert Solution().maxTwoEvents([[10,83,53],[63,87,45],[97,100,32],[51,61,16]]) == 85
assert Solution().maxTwoEvents([[1,5,3],[1,5,1],[6,6,5]]) == 8
assert Solution().maxTwoEvents( [[1,3,2],[4,5,2],[1,5,5]]) == 5
assert Solution().maxTwoEvents([[1, 3, 2], [4, 5, 2], [2, 4, 3]]) == 4


#
# @lcpr case=start
# [[1,3,2],[4,5,2],[2,4,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,2],[4,5,2],[1,5,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,5,3],[1,5,1],[6,6,5]]\n
# @lcpr case=end

#
