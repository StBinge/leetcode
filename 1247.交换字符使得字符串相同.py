#
# @lc app=leetcode.cn id=1247 lang=python3
#
# [1247] 交换字符使得字符串相同
#


# @lc code=start
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        l1=l2=0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == "x":
                    l1+=1
                else:
                    l2+=1

        if (l1 + l2) % 2 == 1:
            return -1

        return l1 // 2 + l2 // 2 + 2 * (l1 & 1)


# @lc code=end
assert Solution().minimumSwap("xx", "xy") == -1
assert Solution().minimumSwap("xx", "yy") == 1
assert Solution().minimumSwap("xy", "yx") == 2
