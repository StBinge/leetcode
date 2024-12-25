#
# @lc app=leetcode.cn id=2343 lang=python3
# @lcpr version=30204
#
# [2343] 裁剪数字后查询第 K 小的数字
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        N=len(queries)
        # L=len(nums[0])
        qindices=sorted(range(N),key=lambda idx:queries[idx][1])
        ret=[0]*N
        j=1
        indices=list(range(len(nums)))
        for qidx in qindices:
            k,trim=queries[qidx]
            while j<=trim:
                indices.sort(key=lambda idx:nums[idx][-j])
                j+=1
            ret[qidx]=indices[k-1]
        return ret
            
# @lc code=end
assert Solution().smallestTrimmedNumbers(nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2],[1,2]])==[2,2,1,0]
assert Solution().smallestTrimmedNumbers(nums = ["24","37","96","04"], queries = [[2,1],[2,2]])==[3,0]


#
# @lcpr case=start
# ["102","473","251","814"]\n[[1,1],[2,3],[4,2],[1,2]]\n
# @lcpr case=end

# @lcpr case=start
# ["24","37","96","04"]\n[[2,1],[2,2]]\n
# @lcpr case=end

#

