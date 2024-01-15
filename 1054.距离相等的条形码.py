#
# @lc app=leetcode.cn id=1054 lang=python3
#
# [1054] 距离相等的条形码
#
from sbw import *
# @lc code=start
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        N=len(barcodes)
        counter=Counter(barcodes)
        orders=sorted(counter.keys(),key=lambda k:counter[k],reverse=True)
        ret=[0]*N
        idx=0
        for code in orders:
            for _ in range(counter[code]):
                ret[idx]=code
                idx+=2
                if idx>=N:
                    idx=1
        return ret
# @lc code=end
ret= Solution().rearrangeBarcodes([1,1,1,1,2,2,3,3])
print(ret)
ret= Solution().rearrangeBarcodes([1,1,1,2,2,2])
print(ret)
