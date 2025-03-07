#
# @lc app=leetcode.cn id=3265 lang=python3
# @lcpr version=30204
#
# [3265] 统计近似相等数对 I
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countPairs(self, nums: List[int]) -> int:
        ret=0
        pow10=[10**i for i in range(7)]
        nums.sort()
        cnt=defaultdict(int)
        for n in nums:
            s=list(map(int,str(n)))[::-1]
            N=len(s)
            for i in range(N):
                for j in range(i+1,N):
                    if s[i]==s[j]:
                        continue
                    y=n+(s[j]-s[i])*pow10[i]+(s[i]-s[j])*pow10[j]
                    ret+=cnt[y]
            ret+=cnt[n]
            cnt[n]+=1
        return ret

# @lc code=end
assert Solution().countPairs([5,12,8,5,5,1,20,3,10,10,5,5,5,5,1])==27
assert Solution().countPairs( [123,231])==0
assert Solution().countPairs([1,1,1,1,1])==10
assert Solution().countPairs( [3,12,30,17,21])==2


#
# @lcpr case=start
# [3,12,30,17,21]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [123,231]\n
# @lcpr case=end

#

