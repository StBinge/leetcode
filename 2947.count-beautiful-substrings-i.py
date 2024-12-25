#
# @lc app=leetcode.cn id=2947 lang=python3
# @lcpr version=30204
#
# [2947] 统计美丽子字符串 I
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vows = "aeiou"

        def sqrt(x: int):
            ret = 1
            i = 2
            while i * i <= x:
                i2 = i * i
                while x % i2 == 0:
                    ret *= i
                    x //= i2
                if x % i == 0:
                    ret *= i
                    x //= i
                i += 1
            if x > 1:
                ret *= x
            return ret

        k = sqrt(4 * k)

        cnt = defaultdict(int)
        cnt[(k - 1, 0)] = 1
        ret = 0
        presum = 0
        for i, ch in enumerate(s):
            presum += 1 if ch in vows else -1
            p = (i % k, presum)
            ret += cnt[p]
            cnt[p] += 1
        return ret


# @lc code=end
assert Solution().beautifulSubstrings("ihroyeeb", 5) == 0
assert Solution().beautifulSubstrings("baeyh", 2) == 2


#
# @lcpr case=start
# "baeyh"\n2\n
# @lcpr case=end

# @lcpr case=start
# "abba"\n1\n
# @lcpr case=end

# @lcpr case=start
# "bcdf"\n1\n
# @lcpr case=end

#
