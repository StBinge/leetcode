#
# @lc app=leetcode.cn id=2527 lang=python3
# @lcpr version=30204
#
# [2527] 查询数组异或美丽值
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        return reduce(lambda x,y:x^y,nums)
# @lc code=end



#
# @lcpr case=start
# [1,4]\n
# @lcpr case=end

# @lcpr case=start
# [15,45,20,2,34,35,5,44,32,30]\n
# @lcpr case=end

#

