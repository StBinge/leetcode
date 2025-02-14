#
# @lc app=leetcode.cn id=3092 lang=python3
# @lcpr version=30204
#
# [3092] 最高频率的 ID
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        cnts=defaultdict(int)
        heap=[]
        ret=[]
        for x,f in zip(nums,freq):
            cnts[x]+=f
            heapq.heappush(heap,[-cnts[x],x])
            while cnts[heap[0][1]]!=-heap[0][0]:
                heapq.heappop(heap)
            ret.append(-heap[0][0] if heap else 0)
        return ret
# @lc code=end



#
# @lcpr case=start
# [2,3,2,1]\n[3,2,-3,1]\n
# @lcpr case=end

# @lcpr case=start
# [5,5,3]\n[2,-2,1]\n
# @lcpr case=end

#

