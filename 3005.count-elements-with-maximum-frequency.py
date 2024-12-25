#
# @lc app=leetcode.cn id=3005 lang=python3
# @lcpr version=30204
#
# [3005] 最大频率元素计数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ret=0
        mx_freg=0
        cnt=Counter(nums)
        for v in cnt.values():
            if v>mx_freg:
                mx_freg=v
                ret=v
            elif v==mx_freg:
                ret+=v
        return ret
# @lc code=end



#
# @lcpr case=start
# [1,2,2,3,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#

