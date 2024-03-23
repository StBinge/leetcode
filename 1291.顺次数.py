#
# @lc app=leetcode.cn id=1291 lang=python3
#
# [1291] 顺次数
#
from sbw import *
# @lc code=start
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ret=[]
        for i in range(1,10):
            num=i
            for j in range(i+1,10):
                num=num*10+j
                if num<low:
                    continue
                if num>high:
                    break
                ret.append(num)
        ret.sort()
        return ret
# @lc code=end
assert Solution().sequentialDigits(low = 1000, high = 13000)==[1234,2345,3456,4567,5678,6789,12345]
assert Solution().sequentialDigits(low = 100, high = 300)==[123,234]
