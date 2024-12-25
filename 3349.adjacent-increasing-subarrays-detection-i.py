#
# @lc app=leetcode.cn id=3349 lang=python3
# @lcpr version=30204
#
# [3349] 检测相邻递增子数组 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        pre_len=cur_len=0
        pre=-2000
        for n in nums:
            if n>pre:
                cur_len+=1
                pre=n
                continue
            if cur_len>=2*k or (cur_len>=k and pre_len>=k):
                return True
            pre_len=cur_len
            cur_len=1
            pre=n
        return cur_len>=2*k or (cur_len>=k and pre_len>=k)

# @lc code=end



#
# @lcpr case=start
# [2,5,7,8,9,2,3,4,3,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,4,4,4,5,6,7]\n5\n
# @lcpr case=end

#

