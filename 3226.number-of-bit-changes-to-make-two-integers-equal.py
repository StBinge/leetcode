#
# @lc app=leetcode.cn id=3226 lang=python3
# @lcpr version=30204
#
# [3226] 使两个整数相等的位更改次数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        xor=n^k
        if xor & n !=xor:
            return -1
        return xor.bit_count()
        
# @lc code=end



#
# @lcpr case=start
# 13\n4\n
# @lcpr case=end

# @lcpr case=start
# 21\n21\n
# @lcpr case=end

# @lcpr case=start
# 14\n13\n
# @lcpr case=end

#

