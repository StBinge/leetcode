#
# @lc app=leetcode.cn id=3346 lang=python3
# @lcpr version=30204
#
# [3346] 执行操作后元素的最高频率 I
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        left=0
        ret=1
        cnt=defaultdict(int)
        cnt_heap=[]
        for right,n in enumerate(nums):
            while n-k>nums[left]+k:
                cnt[nums[left]]-=1
                left+=1
            l=right-left+1
            if l<=numOperations:
                ret=max(ret,l)
            else:
                while cnt_heap:
                    val,k=cnt_heap[0]
                    if cnt[k]!=-val:
                        heapq.heappop(cnt_heap)
                    else:
                        ret=max(ret,min(-val+numOperations,l))
                        break
            cnt[n]+=1
            heapq.heappush(cnt_heap,[-cnt[n],n])
        return ret


# @lc code=end
assert Solution().maxFrequency([1,90],76,1)==1
assert Solution().maxFrequency([88,53],27,2)==2
assert Solution().maxFrequency([88,53],27,2)==2
assert Solution().maxFrequency([2],7,0)==1
assert Solution().maxFrequency(nums = [5,11,20,20], k = 5, numOperations = 1)==2
assert Solution().maxFrequency(nums = [1,4,5], k = 1, numOperations = 2)==2


#
# @lcpr case=start
# [1,4,5]\n1\n2\n
# @lcpr case=end

# @lcpr case=start
# [5,11,20,20]\n5\n1\n
# @lcpr case=end

#

