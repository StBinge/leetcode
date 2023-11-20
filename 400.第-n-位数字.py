#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第 N 位数字
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        if n<10:
            return n
        n-=9
        count=90
        digits=2
        while True:
            total_digits=count*digits
            if n<=total_digits:
                break
            n-=total_digits
            count*=10
            digits+=1
        num_idx,dig_idx=(n-1)//digits,(n-1)%digits
        num=count//9+num_idx
        dig_idx=digits-dig_idx-1
        num//=10**dig_idx
        return num%10
# @lc code=end
assert Solution().findNthDigit(190)==1
assert Solution().findNthDigit(3)==3
assert Solution().findNthDigit(11)==0
assert Solution().findNthDigit(12)==1
