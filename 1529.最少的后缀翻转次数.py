#
# @lc app=leetcode.cn id=1529 lang=python3
#
# [1529] 最少的后缀翻转次数
#


# @lc code=start
class Solution:
    def minFlips(self, target: str) -> int:
        ret=0
        pre='0'
        for cur in target:
            if pre!=cur:
                ret+=1
            pre=cur
        return ret


# @lc code=end

assert Solution().minFlips("00000") == 0
assert Solution().minFlips("101") == 3
assert Solution().minFlips("10111") == 3
