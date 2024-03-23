#
# @lc app=leetcode.cn id=1399 lang=python3
#
# [1399] 统计最大组的数目
#
from sbw import *
# @lc code=start
class Solution:
    def countLargestGroup(self, n: int) -> int:
        sums=defaultdict(int)
        counter=defaultdict(int)
        for i in range(1,n+1):
            sums[i]=sums[i//10]+i%10
            counter[sums[i]]+=1
        ma=0
        ret=0
        for v in counter.values():
            if v>ma:
                ret=1
                ma=v
            elif v==ma:
                ret+=1
        return ret
# @lc code=end
assert Solution().countLargestGroup(15)==6
assert Solution().countLargestGroup(1)==1
assert Solution().countLargestGroup(2)==2
assert Solution().countLargestGroup(13)==4
