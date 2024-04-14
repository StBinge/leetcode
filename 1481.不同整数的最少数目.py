#
# @lc app=leetcode.cn id=1481 lang=python3
#
# [1481] 不同整数的最少数目
#
from sbw import *
# @lc code=start
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter=Counter(arr)
        sorted_cnt=sorted(counter.items(),key=lambda x:x[1])
        for i,[_,cnt] in enumerate(sorted_cnt):
            k-=cnt
            if k<0:
                return len(sorted_cnt)-i
        return 0
# @lc code=end

assert Solution().findLeastNumOfUniqueInts(arr = [4,3,1,1,3,3,2], k = 3)==2
assert Solution().findLeastNumOfUniqueInts(arr = [5,5,4], k = 1)==1