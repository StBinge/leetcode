#
# @lc app=leetcode.cn id=2831 lang=python3
# @lcpr version=30204
#
# [2831] 找出最长等值子数组
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        queues =defaultdict(deque)
        ret=0
        for i,n in enumerate(nums):
            q=queues[n]
            q.append(i)
            while q and i-q[0]+1 -len(q)>k:
                q.popleft()
            ret=max(ret,len(q))
        return ret
# @lc code=end
assert Solution().longestEqualSubarray(nums = [1,1,2,2,1,1], k = 2)==4
assert Solution().longestEqualSubarray(nums = [1,3,2,3,1,3], k = 3)==3


#
# @lcpr case=start
# [1,3,2,3,1,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,2,1,1]\n2\n
# @lcpr case=end

#

