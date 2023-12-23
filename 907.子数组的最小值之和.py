#
# @lc app=leetcode.cn id=907 lang=python3
#
# [907] 子数组的最小值之和
#
from sbw import *
# @lc code=start
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        l=len(arr)
        ret=0
        Mod=10**9+7
        # left=[-1]*l
        # right=[l]*l
        stack=[]
        # def get(idx):
        #     return arr[i] if 0<=i<l else 0
        for i in range(l+1):
            n=arr[i] if i<l else 0
            while stack and arr[stack[-1]]>=n:
                cur=stack.pop()
                # right=i
                left=stack[-1] if stack else -1
                ret+=(i-cur)*(cur-left)*arr[cur]
                ret%=Mod
            # left[i]=stack[-1] if stack else -1
            stack.append(i)
        # stack=[]
        # for i in range(l-1,-1,-1):
        #     n=arr[i]
        #     while stack and arr[stack[-1]]>n:
        #         stack.pop()
        #     right[i]=stack[-1] if stack else l
        #     stack.append(i)
        # for i in range(l):
        #     ret+=(i-left[i])*(right[i]-i)*arr[i]
        #     ret%=Mod
        return ret

# @lc code=end
arr=[71,55,82,55]
assert Solution().sumSubarrayMins(arr)==593

arr = [11,81,94,43,3]
assert Solution().sumSubarrayMins(arr)==444

arr = [3,1,2,4]
assert Solution().sumSubarrayMins(arr)==17
