#
# @lc app=leetcode.cn id=2099 lang=python3
# @lcpr version=30204
#
# [2099] 找到和最大的长度为 K 的子序列
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        for i,n in enumerate(nums):
            if len(heap)<k:
                heapq.heappush(heap,[n,i])            
            elif n>heap[0][0]:
                heapq.heappushpop(heap,[n,i])
        heap.sort(key=lambda x:x[1])
        return [x[0] for x in heap]
# @lc code=end
assert Solution().maxSubsequence([3,4,3,3],2)==[3,4]


#
# @lcpr case=start
# [2,1,3,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [-1,-2,3,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [3,4,3,3]\n2\n
# @lcpr case=end

#

