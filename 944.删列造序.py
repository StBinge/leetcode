#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 删列造序
#
from sbw import *
# @lc code=start
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        R=len(strs)
        if R==1:
            return 0
        C=len(strs[0])
        ret=0
        for c in range(C):
            for r in range(1,R):
                if strs[r][c]<strs[r-1][c]:
                    ret+=1
                    break
        return ret
# @lc code=end
strs = ["zyx","wvu","tsr"]
assert Solution().minDeletionSize(strs)==3
