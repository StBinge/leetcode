#
# @lc app=leetcode.cn id=955 lang=python3
#
# [955] 删列造序 II
#
from sbw import *
# @lc code=start
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ret=0
        R=len(strs)
        # C=len(strs[0])
        cut=[False]*(R-1)
        for col in zip(*strs):
            if all(cut[r] or col[r]<=col[r+1] for r in range(R-1)):
                for r in range(R-1):
                    if col[r]<col[r+1]:
                        cut[r]=True
            else:
                ret+=1
        return ret
# @lc code=end
strs=["xga","xfb","yfa"]
assert Solution().minDeletionSize(strs)==1

strs = ["zyx","wvu","tsr"]
assert Solution().minDeletionSize(strs)==3

strs = ["xc","yb","za"]
assert Solution().minDeletionSize(strs)==0

strs = ["ca","bb","ac"]
assert Solution().minDeletionSize(strs)==1
