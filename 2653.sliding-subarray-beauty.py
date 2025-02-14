#
# @lc app=leetcode.cn id=2653 lang=python3
# @lcpr version=30204
#
# [2653] 滑动子数组的美丽值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class SegTree:
    def __init__(self,mi,mx) -> None:
        self.offset=1-mi
        self.n=mx+self.offset
        self.cnt=[0]*(self.n+1)
    
    def lowbit(self,x):
        return x&-x

    def add(self,x,val=1):
        x+=self.offset
        while x<=self.n:
            self.cnt[x]+=val
            x+=self.lowbit(x)
    
    def query(self,x):
        x+=self.offset
        x=min(x,self.n)
        ret=0
        while x>0:
            ret+=self.cnt[x]
            x-=self.lowbit(x)
        return ret
    
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        N=len(nums)
        mi,mx=min(nums),max(nums)
        if mi>=0:
            return [0]*(N-k+1)
        seg=SegTree(mi,mx)
        for n in nums[:k-1]:
            seg.add(n)
        
        ret=[]
        for i in range(k-1,N):
            seg.add(nums[i])
            negs=seg.query(-1)
            if negs<x:
                ret.append(0)
            else:
                left=mi
                right=-1
                cur=-1
                while left<right:
                    mid=(left+right)>>1
                    if seg.query(mid)>=x:
                        cur=mid
                        right=mid
                    else:
                        left=mid+1
                ret.append(cur)
            seg.add(nums[i-k+1],-1)
        return ret


# @lc code=end
assert Solution().getSubarrayBeauty([-4,0,-1],2,2)==[0,0]
assert Solution().getSubarrayBeauty([-43],1,1)==[-43]
assert Solution().getSubarrayBeauty(nums = [-3,1,2,-3,0,-3], k = 2, x = 1)==[-3,0,-3,-3,-3]
assert Solution().getSubarrayBeauty(nums = [-1,-2,-3,-4,-5], k = 2, x = 2)==[-1,-2,-3,-4]
assert Solution().getSubarrayBeauty(nums = [1,-1,-3,-2,3], k = 3, x = 2)==[-1,-2,-2]


#
# @lcpr case=start
# [1,-1,-3,-2,3]\n3\n2\n
# @lcpr case=end

# @lcpr case=start
# [-1,-2,-3,-4,-5]\n2\n2\n
# @lcpr case=end

# @lcpr case=start
# [-3,1,2,-3,0,-3]\n2\n1\n
# @lcpr case=end

#

