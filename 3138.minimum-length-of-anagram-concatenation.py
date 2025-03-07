#
# @lc app=leetcode.cn id=3138 lang=python3
# @lcpr version=30204
#
# [3138] 同位字符串连接的最小长度
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def minAnagramLength(self, s: str) -> int:
        N=len(s)
        cnt=Counter(s)
        if len(cnt)==1: return 1
        g=reduce(math.gcd,cnt.values())
        for i in range(g,1,-1):
            if N%i:
                continue
            l=N//i
            for j in range(i):
                _cnt=Counter(s[j*l:j*l+l])
                if any(_cnt[k]*i!=v for k,v in cnt.items()):
                    break
            else:
                return l
        return N



# @lc code=end
assert Solution().minAnagramLength("aabbabab") == 4
assert Solution().minAnagramLength("lbuorourlb") == 5
assert Solution().minAnagramLength("abbbaa") == 6
assert Solution().minAnagramLength("jjj") == 1
assert Solution().minAnagramLength("cdef") == 4
assert Solution().minAnagramLength("abba") == 2


#
# @lcpr case=start
# "abba"\n
# @lcpr case=end

# @lcpr case=start
# "cdef"\n
# @lcpr case=end

#
