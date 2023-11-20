#
# @lc app=leetcode.cn id=829 lang=python3
#
# [829] 连续整数求和
#

# @lc code=start
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ret=1
        s=1
        for i in range(2,n):
            d=n-s
            if d<i:
                break
            if d%i==0:
                ret+=1
            s+=i
        return ret
# @lc code=end

assert Solution().consecutiveNumbersSum(5)==2
assert Solution().consecutiveNumbersSum(9)==3
assert Solution().consecutiveNumbersSum(15)==4