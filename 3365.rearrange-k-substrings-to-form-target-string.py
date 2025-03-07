#
# @lc app=leetcode.cn id=3365 lang=python3
# @lcpr version=30204
#
# [3365] 重排子字符串以形成目标字符串
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        N=len(s)
        if k==N:
            return sorted(s)==sorted(t)
        L=N//k
        cnt=Counter([t[i*L:i*L+L] for i in range(k)])
        for i in range(k):
            ss=s[i*L:i*L+L]
            if cnt[ss]==0:
                return False
            cnt[ss]-=1
        return True
# @lc code=end
assert Solution().isPossibleToRearrange(s = "aabbcc", t = "bbaacc", k = 3)==True
assert Solution().isPossibleToRearrange(s = "nc", t = "cn", k = 1)==False
assert Solution().isPossibleToRearrange(s = "aa", t = "aa", k = 2)
assert Solution().isPossibleToRearrange(s = "aabbcc", t = "bbaacc", k = 2)==False
assert Solution().isPossibleToRearrange(s = "abcd", t = "cdab", k = 2)==True


#
# @lcpr case=start
# "abcd"\n"cdab"\n2\n
# @lcpr case=end

# @lcpr case=start
# "aabbcc"\n"bbaacc"\n3\n
# @lcpr case=end

# @lcpr case=start
# "aabbcc"\n"bbaacc"\n2\n
# @lcpr case=end

#

