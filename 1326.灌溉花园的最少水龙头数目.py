#
# @lc app=leetcode.cn id=1326 lang=python3
#
# [1326] 灌溉花园的最少水龙头数目
#
from sbw import *
# @lc code=start
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        right_most=list(range(n+1))
        for i,r in enumerate(ranges):
            left,right=max(0,i-r),min(n,i+r)
            right_most[left]=max(right_most[left],right)
        
        pre=last=ret=0
        for i in range(n):
            last=max(last,right_most[i])
            if last==i:
                return -1
            if pre==i:
                ret+=1
                pre=last
        return ret


# @lc code=end
assert Solution().minTaps(17,[0,3,3,2,2,4,2,1,5,1,0,1,2,3,0,3,1,1])==3
assert Solution().minTaps(8,[4,0,0,0,0,0,0,0,4])==2
assert Solution().minTaps(7,[1,2,1,0,2,1,0,1])==3
assert Solution().minTaps(n = 3, ranges = [0,0,0,0])==-1
assert Solution().minTaps(n = 5, ranges = [3,4,1,1,0,0])==1
