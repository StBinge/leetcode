#
# @lc app=leetcode.cn id=1013 lang=python3
#
# [1013] 将数组分成和相等的三个部分
#
from sbw import *
# @lc code=start
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        # L=len(arr)
 
        S=sum(arr)
        if S % 3:
            return False
        avg=S//3
        cnt=0
        cur=0
        for n in arr:
            cur+=n
            if cur==avg:
                cnt+=1
                if cnt==3:
                    return True
                cur=0
        return False
# @lc code=end
arr = [3,3,6,5,-2,2,5,1,-9,4]
assert Solution().canThreePartsEqualSum(arr)

arr = [0,2,1,-6,6,7,9,-1,2,0,1]
assert not Solution().canThreePartsEqualSum(arr)

arr = [0,2,1,-6,6,-7,9,1,2,0,1]
assert Solution().canThreePartsEqualSum(arr)
