#
# @lc app=leetcode.cn id=2002 lang=python3
# @lcpr version=30204
#
# [2002] 两个回文子序列长度的最大乘积
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProduct(self, s: str) -> int:
        N=len(s)
        valid_masks=[]
        for i in range(1,1<<N):
            chars=[]
            for j in range(N):
                if i & 1<<j:
                    chars.append(s[j])
            if chars==chars[::-1]:
                valid_masks.append([i,len(chars)])
        ret=1
        M=len(valid_masks)
        # Mask=(1<<N)-1
        for i in range(M):
            m1,c1=valid_masks[i]
            for j in range(i+1,M):
                m2,c2=valid_masks[j]
                if m1&m2==0:
                    ret=max(ret,c1*c2)
        return ret
# @lc code=end

assert Solution().maxProduct('accbcaxxcxx')==25
assert Solution().maxProduct('bb')==1
assert Solution().maxProduct('leetcodecom')==9

#
# @lcpr case=start
# "leetcodecom"\n
# @lcpr case=end

# @lcpr case=start
# "bb"\n
# @lcpr case=end

# @lcpr case=start
# "accbcaxxcxx"\n
# @lcpr case=end

#

