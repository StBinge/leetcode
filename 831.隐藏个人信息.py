#
# @lc app=leetcode.cn id=831 lang=python3
#
# [831] 隐藏个人信息
#

# @lc code=start
class Solution:
    def maskPII(self, s: str) -> str:
        phone_chars=set('+-({')
        if s[0] in phone_chars or s[0].isdigit():
            nums=[]
            for c in s:
                if c.isdigit():
                    nums.append(c)
            if len(nums)>10:
                return '+'+'*'*(len(nums)-10)+'-***-***-'+''.join(nums[-4:])
            else:
                return '***-***-'+''.join(nums[-4:])
        
        idx=0

        while s[idx]!='@':
            idx+=1
        name=s[0].lower()+'*****'+s[idx-1].lower()
        return name+s[idx:].lower()
# @lc code=end
s = "1(234)567-890"
ret="***-***-7890"
assert Solution().maskPII(s)==ret

s = "AB@qq.com"
ret="a*****b@qq.com"
assert Solution().maskPII(s)==ret

s="LeetCode@LeetCode.com"
assert Solution().maskPII(s)=="l*****e@leetcode.com"