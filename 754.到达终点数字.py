#
# @lc app=leetcode.cn id=754 lang=python3
#
# [754] 到达终点数字
#

# @lc code=start
from collections import deque
class Solution:
    def reachNumber(self, target: int) -> int:
        target=abs(target)
        left,right=0,target+1
        # s=0
        while left<right:
            mid=(left+right)//2
            s=(1+mid)*mid//2
            if s==target:
                return mid
            elif s<target:
                left=mid+1
            else:
                right=mid
        s=(1+left)*left//2
        if (s-target)%2==0:
            return left
        else:
            return left+1+left%2
# @lc code=end

assert Solution().reachNumber(5)==5
assert Solution().reachNumber(-2)==3
assert Solution().reachNumber(1)==1
assert Solution().reachNumber(4)==3
assert Solution().reachNumber(2)==3
assert Solution().reachNumber(9)==5
assert Solution().reachNumber(3)==2