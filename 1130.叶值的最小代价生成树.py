#
# @lc app=leetcode.cn id=1130 lang=python3
#
# [1130] 叶值的最小代价生成树
#
from sbw import *
# @lc code=start
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # pos={v:i for i,v in enumerate(arr)}
        ret=0
        stack=[]
        for n in arr:
            while stack and stack[-1]<=n:
                x=stack.pop()
                if not stack or stack[-1]>n:
                    ret+=x*n
                else:
                    ret+=x*stack[-1]
            stack.append(n)
        while len(stack)>1:
            ret+=stack.pop()*stack[-1]
        return ret
# @lc code=end
assert Solution().mctFromLeafValues([15,13,5,3,15])==500
assert Solution().mctFromLeafValues([4,11])==44
assert Solution().mctFromLeafValues([6,2,4])==32
