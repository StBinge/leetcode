#
# @lc app=leetcode.cn id=2055 lang=python3
# @lcpr version=30204
#
# [2055] 蜡烛之间的盘子
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        N=len(s)
        pans=[0]
        left_candles=[-1]*N
        right_candles=[N]*N
        if s[0]=='|':
            left_candles[0]=0
        if s[-1]=='|':
            right_candles[-1]=N-1
        for i,ch in enumerate(s):
            p=ch=='*'
            pans.append(p+pans[-1])
        
        for i in range(1,N):
            left_candles[i]=i if s[i]=='|' else left_candles[i-1]
            right_candles[N-1-i]=N-1-i if s[N-1-i]=='|' else right_candles[N-i]


        ret=[]
        for left,right in queries:

            left=right_candles[left]

            right=left_candles[right]
            if left>=right:
                ret.append(0)
            else:
                ret.append(pans[right+1]-pans[left])
        return ret

# @lc code=end

assert Solution().platesBetweenCandles(s = "||*", queries = [[2,2]])==[0]
assert Solution().platesBetweenCandles(s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]])==[9,0,0,0,0]
assert Solution().platesBetweenCandles(s = "**|**|***|", queries = [[2,5],[5,9]])==[2,3]

#
# @lcpr case=start
# "**|**|***|"\n[[2,5],[5,9]]\n
# @lcpr case=end

# @lcpr case=start
# "***|**|*****|**||**|*"\n[[1,17],[4,5],[14,17],[5,11],[15,16]]\n
# @lcpr case=end

#

