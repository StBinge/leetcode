#
# @lc app=leetcode.cn id=2381 lang=python3
# @lcpr version=30204
#
# [2381] 字母移位 II
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N=len(s)
        dif=[0]*(N+1)
        for start,e,d in shifts:
            v=d*2-1
            dif[start]+=v
            dif[e+1]-=v
        
        shift=0
        ret=[]
        for i in range(N):
            shift+=dif[i]
            ret.append(chr((ord(s[i])-97+shift)%26+97))
        return ''.join(ret)
# @lc code=end
assert Solution().shiftingLetters("abc",[[0,1,0],[1,2,1],[0,2,1]])=='ace'


#
# @lcpr case=start
# "abc"\n[[0,1,0],[1,2,1],[0,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# "dztz"\n[[0,0,0],[1,1,1]]\n
# @lcpr case=end

#

