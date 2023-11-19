#
# @lc app=leetcode.cn id=767 lang=python3
#
# [767] 重构字符串
#

# @lc code=start
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter=Counter(s)
        orders=[[v,k] for k,v in counter.items()]
        orders.sort(key=lambda x:x[0],reverse=True)
        N=len(s)
        if 2*orders[0][0]>N+1:
            return ''
        ret=[""]*N
        idx=0
        cid=0
        ch=orders[0][1]
        for cid in range(len(orders)):
            ch=orders[cid][1]
            for _ in range(orders[cid][0]):
                ret[idx]=ch
                idx+=2
                if idx>=N:
                    idx=1
        return ''.join(ret)
# @lc code=end

assert Solution().reorganizeString('aab')=='aba'
assert Solution().reorganizeString('aaab')==''