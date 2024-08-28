#
# @lc app=leetcode.cn id=2007 lang=python3
# @lcpr version=30204
#
# [2007] 从双倍数组中还原原数组
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []
        Mx=max(changed)
        cnt =[0]*(Mx+1)
        for n in changed:
            cnt[n]+=1
        if cnt[0]%2:
            return []
        ret = [0]*(cnt[0]//2)

        for n in range(1,Mx+1):
            if cnt[n]==0:
                continue
            if n<<1>Mx or cnt[n]>cnt[n<<1]:
                return []
            ret.extend([n]*cnt[n])
            cnt[n<<1]-=cnt[n]
        if len(ret) == len(changed) // 2:
            return ret
        return []


# @lc code=end
assert Solution().findOriginalArray([3,3,3,3]) == []
assert Solution().findOriginalArray([4,4,16,20,8,8,2,10]) == [2,4,8,10]
assert Solution().findOriginalArray([2,1,2,4,2,4]) == [1,2,2]
assert Solution().findOriginalArray([1]) == []
assert Solution().findOriginalArray([6,3,0,1]) == []
assert Solution().findOriginalArray([1, 3, 4, 2, 6, 8]) == [1, 3, 4]


#
# @lcpr case=start
# [1,3,4,2,6,8]\n
# @lcpr case=end

# @lcpr case=start
# [6,3,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
