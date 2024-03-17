#
# @lc app=leetcode.cn id=1442 lang=python3
#
# [1442] 形成两个异或相等数组的三元组数目
#
from sbw import *
# @lc code=start
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        xor=0
        cnt=Counter()
        s=Counter()
        ret=0
        for i,n in enumerate(arr):
            _xor=xor^n
            ret+=cnt[_xor]*i-s[_xor]
            cnt[xor]+=1
            s[xor]+=i
            xor=_xor
        return ret

# @lc code=end
assert Solution().countTriplets([2,3])==0
assert Solution().countTriplets([1,1,1,1,1])==10
assert Solution().countTriplets([2,3,1,6,7])==4
