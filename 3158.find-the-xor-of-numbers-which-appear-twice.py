#
# @lc app=leetcode.cn id=3158 lang=python3
# @lcpr version=30204
#
# [3158] 求出出现两次数字的 XOR 值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        seen=set()
        ret=0
        for n in nums:
            if n in seen:
                ret^=n
            else:
                seen.add(n)
        return ret
# @lc code=end



#
# @lcpr case=start
# [1,2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

#

