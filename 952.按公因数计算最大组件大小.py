#
# @lc app=leetcode.cn id=952 lang=python3
#
# [952] 按公因数计算最大组件大小
#
from sbw import *
# @lc code=start
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        p=list(range(max(nums)+1))
        sz=[1]*len(p)
        ss=set(nums)
        
        def find(x):
            if x!=p[x]:
                p[x]=find(p[x])
            return p[x]
        
        def connect(x,y):
            px,py=find(x),find(y)
            if px==py:
                return
            if sz[px]>sz[py]:
                p[py]=px
                sz[px]+=sz[py]
            else:
                p[px]=py
                sz[py]+=sz[px]


        for n in nums:
            i=2
            while i*i<=n:
                if n%i==0:
                    if i in ss:
                        connect(n,i)
                    if n//i in ss:
                        connect(n,n//i)
                i+=1

        # return max(Counter(find(x) for x in nums).values())


        s=1
        return max(sz[n] for n in nums)
# @lc code=end
nums = [2,3,6,7,4,12,21,39]
assert Solution().largestComponentSize(nums)==8

nums = [20,50,9,63]
assert Solution().largestComponentSize(nums)==2

nums = [4,6,15,35]
assert Solution().largestComponentSize(nums)==4