#
# @lc app=leetcode.cn id=1128 lang=python3
#
# [1128] 等价多米诺骨牌对的数量
#
from sbw import *
# @lc code=start
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt=[0]*100
        ret=0
        for a,b in dominoes:
            if a>b:
                t=a*10+b
            else:
                t=b*10+a
            ret+=cnt[t]
            cnt[t]+=1
        return ret
# @lc code=end
assert Solution().numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]])==3
assert Solution().numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]])==1
