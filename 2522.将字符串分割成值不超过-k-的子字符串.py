#
# @lc app=leetcode.cn id=2522 lang=python3
#
# [2522] 将字符串分割成值不超过 K 的子字符串
#
from sbw import *
# @lc code=start
import math
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        L=len(s)
        ret=1
        n=0
        for i in range(L):
            cur= n*10+int(s[i])
            if cur>k:
                n=int(s[i])
                if n>k:
                    return -1
                ret+=1
            else:
                n=cur
        return ret
# @lc code=end
assert Solution().minimumPartition('21372772',17)==7
assert Solution().minimumPartition('238182',5)==-1
assert Solution().minimumPartition('165462',60)==4
