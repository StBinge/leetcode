#
# @lc app=leetcode.cn id=1090 lang=python3
#
# [1090] 受标签影响的最大值
#
from sbw import *
# @lc code=start
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        L=len(values)
        ordered_pos=sorted(range(L),key=values.__getitem__)
        label_cnt=Counter()
        ret=0
        
        while numWanted>0 and ordered_pos:
            idx=ordered_pos.pop()
            label=labels[idx]
            if label_cnt[label]<useLimit:
                ret+=values[idx]
                label_cnt[label]+=1
                numWanted-=1
        return ret

# @lc code=end
assert Solution().largestValsFromLabels(values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1)==16
assert Solution().largestValsFromLabels(values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2)==12
assert Solution().largestValsFromLabels(values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1)==9
