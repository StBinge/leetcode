#
# @lc app=leetcode.cn id=2595 lang=python3
# @lcpr version=30204
#
# [2595] 奇偶位数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even=0b010101010101
        odd=0b101010101010
        return [(n&even).bit_count(),(n&odd).bit_count()]
# @lc code=end
assert Solution().evenOddBit(2)==[0,1]
assert Solution().evenOddBit(50)==[1,2]
assert Solution().evenOddBit(17)==[2,0]


#
# @lcpr case=start
# 17\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#

