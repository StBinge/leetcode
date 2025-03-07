#
# @lc app=leetcode.cn id=2767 lang=python3
# @lcpr version=30204
#
# [2767] 将字符串分割为最少的美丽子字符串
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        if s[0] == "0":
            return -1
        Mask=5**6

        N = len(s)
        f=[float('inf')]*(N+1)
        f[0]=0
        for i in range(N):
            v=0
            for j in range(i,-1,-1):
                if s[j]=='0':
                    continue
                v+=((ord(s[j])&1)<<(i-j))
                if Mask % v==0:
                    f[i+1]=min(f[i+1],f[j]+1)
        return f[-1] if f[-1] < float("inf") else -1


# @lc code=end
assert Solution().minimumBeautifulSubstrings("1011") == 2
assert Solution().minimumBeautifulSubstrings("111") == 3
assert Solution().minimumBeautifulSubstrings("0") == -1


#
# @lcpr case=start
# "1011"\n
# @lcpr case=end

# @lcpr case=start
# "111"\n
# @lcpr case=end

# @lcpr case=start
# "0"\n
# @lcpr case=end

#
