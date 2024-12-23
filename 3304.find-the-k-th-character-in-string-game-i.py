#
# @lc app=leetcode.cn id=3304 lang=python3
# @lcpr version=30204
#
# [3304] 找出第 K 个字符 I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def kthCharacter(self, k: int) -> str:
        return chr(ord('a')+(k-1).bit_count())

        
# @lc code=end
assert Solution().kthCharacter(10)=='c'
assert Solution().kthCharacter(5)=='b'


#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 10\n
# @lcpr case=end

#

