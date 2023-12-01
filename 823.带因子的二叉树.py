#
# @lc app=leetcode.cn id=823 lang=python3
#
# [823] 带因子的二叉树
#
from typing import List
# @lc code=start
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        L=len(arr)
        d=[1]*L
        MOD=10**9+7
        ret=0
        for i,n in enumerate(arr):
            left,right=0,i-1
            while left<=right:
                while right>=left and arr[right]*arr[left]>n:
                    right-=1
                if right>=left and arr[left]*arr[right]==n:
                    cnt=d[left]*d[right]
                    if left!=right:
                        cnt*=2
                    d[i]+=cnt
                    d[i]%=MOD
                left+=1
            ret+=d[i]
            ret%=MOD
        return ret





# @lc code=end
arr = [2, 4, 5, 10]
assert Solution().numFactoredBinaryTrees(arr)==7

arr=[2,4]
assert Solution().numFactoredBinaryTrees(arr)==3