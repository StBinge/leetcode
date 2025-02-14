#
# @lc app=leetcode.cn id=2785 lang=python3
# @lcpr version=30204
#
# [2785] 将字符串中的元音字母排序
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def sortVowels(self, s: str) -> str:
        N=len(s)
        ret=['']*N
        idx=0
        vows='aeiou'
        for ch in sorted([ch for ch in s if ch.lower() in vows]):
            while s[idx].lower() not in vows:
                ret[idx]=s[idx]
                idx+=1
            ret[idx]=ch
            idx+=1
        while idx<N:
            if s[idx].lower() not in vows:
                ret[idx]=s[idx]
            idx+=1
        return ''.join(ret)
# @lc code=end
assert Solution().sortVowels("LQRamBOHfq")=="LQROmBaHfq"


#
# @lcpr case=start
# "lEetcOde"\n
# @lcpr case=end

# @lcpr case=start
# "lYmpH"\n
# @lcpr case=end

#

