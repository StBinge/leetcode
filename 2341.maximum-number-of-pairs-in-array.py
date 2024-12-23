#
# @lc app=leetcode.cn id=2341 lang=python3
# @lcpr version=30204
#
# [2341] 数组能形成多少数对
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cnt=Counter(nums)
        pairs=sum(v//2 for v in cnt.values())
        return [pairs,len(nums)-pairs*2]
# @lc code=end



#
# @lcpr case=start
# [1,3,2,1,3,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

