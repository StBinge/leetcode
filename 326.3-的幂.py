#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3 的幂
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        Max=3**19
        return n>0 and Max % n==0
# @lc code=end
assert Solution().isPowerOfThree(1)
assert Solution().isPowerOfThree(27)
assert Solution().isPowerOfThree(0)==False
assert Solution().isPowerOfThree(45)==False
assert Solution().isPowerOfThree(9)==True
