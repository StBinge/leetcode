#
# @lc app=leetcode.cn id=3335 lang=python3
# @lcpr version=30204
#
# [3335] 字符串转换后的长度 I
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod=10**9+7
        cnt=[0]*26
        for ch in s:
            cnt[ord(ch)-97]+=1
        for _ in range(t):
            z=cnt[-1]
            for i in range(25,0,-1):
                cnt[i]=cnt[i-1]
            cnt[1]=(cnt[1]+z)%mod
            cnt[0]=z
        return sum(cnt)%mod

# @lc code=end
assert Solution().lengthAfterTransformations("jqktcurgdvlibczdsvnsg",7517)==79033769
assert Solution().lengthAfterTransformations(s = "azbk", t = 1)==5
assert Solution().lengthAfterTransformations( s = "abcyy", t = 2)==7


#
# @lcpr case=start
# "abcyy"\n2\n
# @lcpr case=end

# @lcpr case=start
# "azbk"\n1\n
# @lcpr case=end

#

