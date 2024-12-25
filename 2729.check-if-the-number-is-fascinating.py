#
# @lc app=leetcode.cn id=2729 lang=python3
# @lcpr version=30204
#
# [2729] 判断一个数是否迷人
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isFascinating(self, n: int) -> bool:
        if n*3>999:
            return False
        s=set(str(n))
        s.update(str(n*2))
        s.update(str(n*3))
        return len(s)==9 and '0' not in s

# @lc code=end
assert Solution().isFascinating(783)==False


#
# @lcpr case=start
# 192\n
# @lcpr case=end

# @lcpr case=start
# 100\n
# @lcpr case=end

#

