#
# @lc app=leetcode.cn id=2745 lang=python3
# @lcpr version=30204
#
# [2745] 构造最长的新字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        return (min(x,y)*2+z+(x!=y))*2


# @lc code=end
assert Solution().longestString(3,2,2)==14
assert Solution().longestString(x = 2, y = 5, z = 1)==12
assert Solution().longestString(x = 2, y = 5, z = 1)==12


#
# @lcpr case=start
# 2\n5\n1\n
# @lcpr case=end

# @lcpr case=start
# 3\n2\n2\n
# @lcpr case=end

#

