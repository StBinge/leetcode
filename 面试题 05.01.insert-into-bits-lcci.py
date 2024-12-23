#
# @lc app=leetcode.cn id=面试题 05.01 lang=python3
# @lcpr version=30204
#
# [面试题 05.01] 插入
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        tail=N & (1<<i)-1
        j+=1
        N=(N>>j)<<j
        ret= N|(M<<i)|tail
        return ret
# @lc code=end
assert Solution().insertBits(2032243561,10,24,29)==1243714409
assert Solution().insertBits(1024,19,2,6)==1100


#
# @lcpr case=start
# 1024(10000000000)\n19(10011)\n2\n6\n
# @lcpr case=end

# @lcpr case=start
# 0\n31(11111)\n0\n4\n
# @lcpr case=end

#

