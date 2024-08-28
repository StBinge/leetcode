#
# @lc app=leetcode.cn id=1906 lang=python3
# @lcpr version=30204
#
# [1906] 查询差绝对值的最小值
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        Max=max(nums)
        pos_list=[[] for _ in range(Max+1)]
        for i,n in enumerate(nums):
            pos_list[n].append(i)
        
        ret=[]
        for l,r in queries:
            pre=0
            dif=101
            for i in range(1,Max+1):
                ps=pos_list[i]
                if not ps:
                    continue
                cnt=bisect_right(ps,r)-bisect_left(ps,l)
                if not cnt:
                    continue
                if cnt==r-l+1:
                    ret.append(-1)
                    break


                if pre:
                    dif=min(dif,i-pre)
                    if dif==1:
                        ret.append(1)
                        break
                    pre=i
                else:
                    pre=i
            else:
                ret.append(dif)
        return ret


        
# @lc code=end

assert Solution().minDifference(nums = [4,5,2,2,7,10], queries = [[2,3],[0,2],[0,5],[3,5]])==[-1,1,1,3]
assert Solution().minDifference(nums = [1,3,4,8], queries = [[0,1],[1,2],[2,3],[0,3]])==[2,1,4,1]

#
# @lcpr case=start
# [1,3,4,8]\n[[0,1],[1,2],[2,3],[0,3]]\n
# @lcpr case=end

# @lcpr case=start
# [4,5,2,2,7,10]\n[[2,3],[0,2],[0,5],[3,5]]\n
# @lcpr case=end

#

