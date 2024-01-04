#
# @lc app=leetcode.cn id=1051 lang=python3
#
# [1051] 高度检查器
#
from sbw import *
# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        mi,ma=100,0
        for h in heights:
            mi=min(mi,h)
            ma=max(ma,h)
        cnt=[0]*(ma-mi+1)
        for h in heights:
            cnt[h-mi]+=1
        ans=idx=0
        for i in range(ma-mi+1):
            h=i+mi
            for _ in range(cnt[i]):
                if heights[idx]!=h:
                    ans+=1
                idx+=1
        return ans
# @lc code=end
assert Solution().heightChecker([2,1,2,1,1,2,2,1])==4

heights = [1,2,3,4,5]
assert Solution().heightChecker(heights)==0

heights = [5,1,2,3,4]
assert Solution().heightChecker(heights)==5

heights = [1,1,4,2,1,3]
assert Solution().heightChecker(heights)==3
