#
# @lc app=leetcode.cn id=2980 lang=python3
# @lcpr version=30204
#
# [2980] 检查按位或是否存在尾随零
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        cnt=0
        for n in nums:
            cnt+=n&1==0
            if cnt>1:
                return True
        return False
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [2,4,8,16]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,7,9]\n
# @lcpr case=end

#

