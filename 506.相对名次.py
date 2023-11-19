#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#
from typing import List
# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ward=["Gold Medal","Silver Medal","Bronze Medal"]
        ps=sorted(enumerate(score),key=lambda x:x[1],reverse=True)
        ret=[None]*len(score)
        # cnt=1
        for i in range(len(ps)):
            ret[ps[i][0]]=ward[i] if i<3 else str(i+1)
        return ret
# @lc code=end
assert Solution().findRelativeRanks([10,3,8,9,4])==["Gold Medal","5","Bronze Medal","Silver Medal","4"]
assert Solution().findRelativeRanks([5,4])==["Gold Medal","Silver Medal"]
assert Solution().findRelativeRanks([5,4,3,2,1])==["Gold Medal","Silver Medal","Bronze Medal","4","5"]
