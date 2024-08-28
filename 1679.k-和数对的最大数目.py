#
# @lc app=leetcode.cn id=1679 lang=python3
#
# [1679] K 和数对的最大数目
#
from sbw import *
# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter=defaultdict(int)
        ret=0
        for n in nums:
            if n>=k:
                continue
            m=k-n
            if counter[m]:
                ret+=1
                counter[m]-=1
            else:
                counter[n]+=1
        return ret
# @lc code=end

