#
# @lc app=leetcode.cn id=866 lang=python3
#
# [866] 回文素数
#

# @lc code=start
class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x):
            if x<2:
                return False
            i=2
            while i*i<=x:
                if x%i==0:
                    return False
                i+=1
            return True
        
        for l in range(len(str(n)),10):
            half_l=(l+1)//2
            # if 
            for i in range(10**(half_l-1),10**half_l):
                r=str(i)
                f=r+(r[-2::-1] if l&1 else r[::-1])
                x=int(f)
                if x>=n and is_prime(x):
                    return x
            
            
# @lc code=end

assert Solution().primePalindrome(9989900)==100030001
assert Solution().primePalindrome(102)==131
assert Solution().primePalindrome(1)==2
assert Solution().primePalindrome(11)==11
assert Solution().primePalindrome(13)==101
assert Solution().primePalindrome(8)==11
assert Solution().primePalindrome(6)==7