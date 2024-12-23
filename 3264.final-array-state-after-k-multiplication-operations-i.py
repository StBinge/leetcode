#
# @lc app=leetcode.cn id=3264 lang=python3
# @lcpr version=30204
#
# [3264] K 次乘运算后的最终数组 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier==1:
            return nums
        mx=max(nums)
        heap=[[n,i] for i,n in enumerate(nums)]
        heapq.heapify(heap)
        while k and heap[0][0]!=mx:
            x,idx=heap[0]
            heapq.heapreplace(heap,[x*multiplier,idx])
            k-=1
        if k>0:
            k,m=divmod(k,len(nums))
            muls=pow(multiplier,k)
            heap.sort()
            for i in range(len(nums)):
                x,idx=heap[i]
                heap[i][0]=x*muls*(multiplier if i<m else 1)
        for x,idx in heap:
            nums[idx]=x
        return nums
        
# @lc code=end
assert Solution().getFinalState([1,2],3,4)


#
# @lcpr case=start
# [2,1,3,5,6]\n5\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n3\n4\n
# @lcpr case=end

#

