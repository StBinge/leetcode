#
# @lc app=leetcode.cn id=2163 lang=python3
# @lcpr version=30204
#
# [2163] 删除元素后和的最小差值
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from sortedcontainers import SortedList


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums)
        n = N // 3
        max_suf=[0]*(n+1)
        right_heap=nums[-n:]
        heapq.heapify(right_heap)
        right_sum=sum(right_heap)
        max_suf[-1]=right_sum
        for i in range(N-n-1,n-1,-1):
            x=nums[i]
            right_sum+=x
            right_sum-=heapq.heappushpop(right_heap,x)
            max_suf[i-n]=right_sum
        
        left_heap=[-x for x in nums[:n]]
        heapq.heapify(left_heap)
        left_sum=sum(left_heap)
        ret=max_suf[0]+left_sum
        for i in range(n,2*n):
            x=-nums[i]
            left_sum+=x
            left_sum-=heapq.heappushpop(left_heap,x)
            ret=max(ret,max_suf[i-n+1]+left_sum)
        return -ret



# @lc code=end

assert Solution().minimumDifference([7, 9, 5, 8, 1, 3]) == 1
assert Solution().minimumDifference(nums=[3, 1, 2]) == -1


#
# @lcpr case=start
# [3,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [7,9,5,8,1,3]\n
# @lcpr case=end

#
