#
# @lc app=leetcode.cn id=1994 lang=python3
# @lcpr version=30204
#
# [1994] 好子集的数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        mods=10**9+7
        #        0 1 2 3 4  5  6  7  8  9
        primes= [2,3,5,7,11,13,17,19,23,29]
        invalids=[1,4,8,12,16,20,24,28,9,18,27,16,25]
        counter=[0]*31
        for n in nums:
            counter[n]+=1
        valid_nums=[]
        valid_masks=[]
        for i,c in enumerate(counter):
            if c==0 or i in invalids:
                continue
            m=0
            for j in range(10):
                if i%primes[j]==0:
                    m|=1<<j
            valid_nums.append(i)
            valid_masks.append(m)

        mask=1<<10
        f=[0]*mask
        f[0]=pow(2,counter[1],mods)
        for i,num in enumerate(valid_nums):
            cur=valid_masks[i]
            for prev in range(mask-1,-1,-1):
                if prev&cur:
                    continue
                f[cur|prev]=(f[cur|prev]+f[prev]*counter[num])%mods
        return sum(f[1:])%mods
        
# @lc code=end
assert Solution().numberOfGoodSubsets([5,10,1,26,24,21,24,23,11,12,27,4,17,16,2,6,1,1,6,8,13,30,24,20,2,19])==5368
assert Solution().numberOfGoodSubsets([12,3])==1
assert Solution().numberOfGoodSubsets( [4,2,3,15])==5
assert Solution().numberOfGoodSubsets([1,2,3,4])==6


#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,3,15]\n
# @lcpr case=end

#

