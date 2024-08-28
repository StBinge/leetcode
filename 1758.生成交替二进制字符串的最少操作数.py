#
# @lc app=leetcode.cn id=1758 lang=python3
#
# [1758] 生成交替二进制字符串的最少操作数
#


# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        cnt=sum(int(ch)==i&1 for i,ch in enumerate(s))
        return min(cnt,len(s)-cnt)


# @lc code=end
assert Solution().minOperations("1111") == 2
assert Solution().minOperations("10") == 0
assert Solution().minOperations("0100") == 1
