#
# @lc app=leetcode.cn id=868 lang=python3
#
# [868] 二进制间距
#


# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        ret = 0
        last=-1
        i=0
        while n:
            if n&1:
                if last!=-1:
                    ret=max(ret,i-last)
                last=i

            n>>=1
            i+=1
        return ret


# @lc code=end
assert Solution().binaryGap(5) == 2
assert Solution().binaryGap(22) == 2
assert Solution().binaryGap(8) == 0
