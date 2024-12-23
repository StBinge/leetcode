#
# @lc app=leetcode.cn id=2575 lang=python3
# @lcpr version=30204
#
# [2575] 找出字符串的可整除数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        r=0
        ret=[0]*len(word)
        for i,ch in enumerate(word):
            r=(r*10+int(ch))%m
            ret[i]=int(r%m==0)
        return ret
# @lc code=end
assert Solution().divisibilityArray('998244353',3)==[1,1,0,0,0,1,1,0,0]


#
# @lcpr case=start
# "998244353"\n3\n
# @lcpr case=end

# @lcpr case=start
# "1010"\n10\n
# @lcpr case=end

#

