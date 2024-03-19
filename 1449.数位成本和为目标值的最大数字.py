#
# @lc app=leetcode.cn id=1449 lang=python3
#
# [1449] 数位成本和为目标值的最大数字
#
from sbw import *
# @lc code=start
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        f=[float('-inf')]*(target+1)
        f[0]=0
        for t in range(1,target+1):
            for i in range(9):
                u=cost[i]
                if t-u>=0:
                    f[t]=max(f[t],1+f[t-u])

        if f[target]<0:
            return '0'
        
        ans=''
        for i in range(8,-1,-1):
            u=cost[i]
            while target>=u and f[target]==f[target-u]+1:
                ans+=str(i+1)
                target-=u
        return ans

# @lc code=end
assert Solution().largestNumber(cost = [6,10,15,40,40,40,40,40,40], target = 47)=='32211'
assert Solution().largestNumber(cost = [2,4,6,2,4,6,4,4,4], target = 5)=='0'
assert Solution().largestNumber(cost = [7,6,5,5,5,6,8,7,8], target = 12)=='85'
assert Solution().largestNumber(cost = [4,3,2,5,6,7,2,5,5], target = 9)=='7772'
