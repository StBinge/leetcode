#
# @lc app=leetcode.cn id=762 lang=python3
#
# [762] 二进制表示中质数个计算置位
#

# @lc code=start
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime={2,3,5,7,11,13,17,19}
        ret=0
        for i in range(left, right+1):
            cnt=0
            while i:
                i&=i-1
                cnt+=1
            if cnt in prime:
                ret+=1
        return ret
# @lc code=end
assert Solution().countPrimeSetBits(6,10)==4
assert Solution().countPrimeSetBits(10,15)==5
