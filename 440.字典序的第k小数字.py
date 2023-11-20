#
# @lc app=leetcode.cn id=440 lang=python3
#
# [440] 字典序的第K小数字
#

# @lc code=start
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def step(cur,n):
            steps=0
            first,last=cur,cur
            while first<=n:
                steps+=min(last,n)-first+1
                first*=10
                last=last*10+9
            return steps
        
        cur=1
        # k-=1
        while k>1:
            steps=step(cur,n)
            if steps<k:
                k-=steps
                cur+=1
            else:
                cur*=10
                k-=1
        return cur
            
# @lc code=end

assert Solution().findKthNumber(100,10)==17
assert Solution().findKthNumber(13,2)==10
assert Solution().findKthNumber(1,1)==1