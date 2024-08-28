#
# @lc app=leetcode.cn id=1646 lang=python3
#
# [1646] 获取生成数组中的最大值
#


# @lc code=start
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n
        f = [0] * (n + 1)
        f[1] = 1
        ret = 1
        for i in range(2, n + 1):
            if i & 1:
                f[i] = f[i // 2] + f[i // 2 + 1]
                ret = max(ret, f[i])
            else:
                f[i] = f[i // 2]
        return ret


# @lc code=end
assert Solution().getMaximumGenerated(15) == 5
assert Solution().getMaximumGenerated(7) == 3
