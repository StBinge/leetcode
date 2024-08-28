#
# @lc app=leetcode.cn id=2094 lang=python3
# @lcpr version=30204
#
# [2094] 找出 3 位偶数
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt=[0]*10
        for d in digits:
            cnt[d]+=1
        evens=[i for i in range(0,10,2) if cnt[i]>0]
        if not evens:
            return []
        ret=[]
        for i in range(1,10):
            if cnt[i]==0:
                continue
            cnt[i]-=1
            for j in range(10):
                if cnt[j]==0:
                    continue
                cnt[j]-=1
                for k in evens:
                    if cnt[k]==0:
                        continue
                    ret.append(i*100+j*10+k)
                cnt[j]+=1
            cnt[i]+=1
        return ret

# @lc code=end



#
# @lcpr case=start
# [2,1,3,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,8,8,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,7,5]\n
# @lcpr case=end

#

