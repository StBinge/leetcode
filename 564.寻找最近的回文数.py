#
# @lc app=leetcode.cn id=564 lang=python3
#
# [564] 寻找最近的回文数
#

# @lc code=start
class Solution:
    def nearestPalindromic(self, n: str) -> str:
               
        L=len(n)
        canidates=[10**(L-1)-1,10**L+1]

        prefix=int(n[:(L+1)//2])

        for x in range(prefix-1,prefix+2):
            y=x if L%2==0 else x//10
            while y:
                x=x*10+y%10
                y//=10
            canidates.append(x)
        
        dif=float('inf')
        ret=-1
        n=int(n)
        for num in canidates:
            if num==n:
                continue
            if abs(num-n)<dif:
                dif=abs(num-n)
                ret=num
        return str(ret)

            
        
                    

# @lc code=end

assert Solution().nearestPalindromic('1213')=='1221'
assert Solution().nearestPalindromic('123')=='121'
assert Solution().nearestPalindromic('1')=='0'