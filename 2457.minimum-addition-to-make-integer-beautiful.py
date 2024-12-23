#
# @lc app=leetcode.cn id=2457 lang=python3
# @lcpr version=30204
#
# [2457] 美丽整数的最小增量
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        digits=[]
        while n:
            digits.append(n%10)
            n//=10
        digits.append(0)
        s=sum(digits)
        ret=0
        idx=0
        while s>target:
            if digits[idx]==0:
                idx+=1
                continue
            ret+=(10-digits[idx])*(10**idx)
            s-=digits[idx]
            idx+=1
            carry=1
            while carry:
                if digits[idx]==9:
                    s-=digits[idx]
                    idx+=1
                else:
                    digits[idx]+=1
                    carry=0
                    s+=1
        return ret
        

# @lc code=end
assert Solution().makeIntegerBeautiful(94598,6)==5402
assert Solution().makeIntegerBeautiful(590,1)==410
assert Solution().makeIntegerBeautiful(1,1)==0
assert Solution().makeIntegerBeautiful(467,6)==33
assert Solution().makeIntegerBeautiful(16,6)==4


#
# @lcpr case=start
# 16\n6\n
# @lcpr case=end

# @lcpr case=start
# 467\n6\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

#

