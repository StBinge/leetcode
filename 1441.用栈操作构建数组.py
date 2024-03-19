#
# @lc app=leetcode.cn id=1441 lang=python3
#
# [1441] 用栈操作构建数组
#
from sbw import *
# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ret=[]
        push="Push"
        pop='Pop'
        cur=1
        for n in target:
            dif=n-cur
            ret.extend([push,pop]*dif)
            ret.append(push)
            cur=n+1
        return ret
# @lc code=end
assert Solution().buildArray(target = [1,2], n = 4)==["Push","Push"]
assert Solution().buildArray(target = [1,2,3], n = 3)==["Push","Push","Push"]
assert Solution().buildArray(target = [1,3], n = 3)==["Push","Push","Pop","Push"]
