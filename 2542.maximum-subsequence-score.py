#
# @lc app=leetcode.cn id=2542 lang=python3
# @lcpr version=30204
#
# [2542] 最大子序列的分数
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        sorted_pairs=sorted(zip(nums1,nums2),key=lambda x:-x[1])
        heap=[x[0] for x in sorted_pairs[:k]]
        heapq.heapify(heap)
        s=sum(heap)
        ret=sorted_pairs[k-1][1]*s
        for i in range(k,len(nums1)):
            n1,n2=sorted_pairs[i]
            if n1>heap[0]:
                s+=n1-heapq.heapreplace(heap,n1)
            ret=max(ret,n2*s)
        return ret

# @lc code=end
assert Solution().maxScore([22,5,25,15,28,1],[22,30,25,25,9,18],3)==1364
assert Solution().maxScore([2,1,14,12],[11,7,13,6],3)==168
assert Solution().maxScore(nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1)==30
assert Solution().maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3)==12


#
# @lcpr case=start
# [1,3,3,2]\n[2,1,3,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [4,2,3,1,1]\n[7,5,10,9,6]\n1\n
# @lcpr case=end

#

