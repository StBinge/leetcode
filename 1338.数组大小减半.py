#
# @lc app=leetcode.cn id=1338 lang=python3
#
# [1338] 数组大小减半
#
from sbw import *
# @lc code=start
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        L=len(arr)
        counter=Counter(arr)
        ret=0
        tot=0
        for cnt in sorted(counter.values(),reverse=True):
            tot+=cnt
            ret+=1
            if tot*2>=L:
                return ret
        
# @lc code=end
assert Solution().minSetSize([7,7,7,7,7,7])==1
assert Solution().minSetSize([3,3,3,3,5,5,5,2,2,7])==2

