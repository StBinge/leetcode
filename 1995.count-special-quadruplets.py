#
# @lc app=leetcode.cn id=1995 lang=python3
# @lcpr version=30204
#
# [1995] 统计特殊四元组
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # N = len(nums)
        # 计入当前元素, 使用k个元素, 能够凑成的值
        f=[[0]*4 for _ in range(101)]
        f[0][0]=1
        ret=0
        for i,n in enumerate(nums):
            ret+=f[n][3]
            for j in range(100,0,-1):
                for k in range(4):
                    if j-n>=0 and k>0:
                        f[j][k]+=f[j-n][k-1]
        return ret

# @lc code=end
def func(nums):
    N=len(nums)
    idx=1
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                for m in range(k+1,N):
                    if nums[i]+nums[j]+nums[k]==nums[m]:
                        # print(idx)
                        idx+=1
                        # print(i,j,k,m)
                        # print(nums[i],nums[j],nums[k],nums[m])
                        # print(nums[i]+nums[j])

func([39,24,31,94,8,54,83,49,43,2,72,100,49,69,40,47,60,26])

assert Solution().countQuadruplets([39,24,31,94,8,54,83,49,43,2,72,100,49,69,40,47,60,26]) == 5
assert Solution().countQuadruplets([1,1,1,3,5]) == 4
assert Solution().countQuadruplets([3,3,6,4,5]) == 0
assert Solution().countQuadruplets([1, 2, 3, 6]) == 1


#
# @lcpr case=start
# [1,2,3,6]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,6,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,3,5]\n
# @lcpr case=end

#
