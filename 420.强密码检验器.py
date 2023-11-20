#
# @lc app=leetcode.cn id=420 lang=python3
#
# [420] 强密码检验器
#
from typing import List
# @lc code=start
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        L=len(password)
        has_lower=False
        has_upper=False
        has_number=False
        for ch in password:
            if ch.islower():
                has_lower=True
            elif ch.isupper():
                has_upper=True
            elif ch.isnumeric():
                has_number=True
        categories=has_lower+has_upper+has_number
        if L<6:
            return max(6-L,3-categories)
        if L<=20:
            pre=''
            cnt=1
            replace=0
            idx=0
            while idx<L:
                while idx<L and password[idx]==pre:
                    idx+=1
                    cnt+=1
                if cnt>=3:
                    replace+=cnt//3
                if idx<L:
                    pre=password[idx]
                    cnt=1
                    idx+=1
            return max(replace,3-categories)
        
        replace=0
        remove=L-20
        rm2=0
        idx=0
        pre=''
        cnt=1
        while idx<L:
            while idx<L and password[idx]==pre:
                idx+=1
                cnt+=1

            if cnt>=3:
                replace+=cnt//3
                if cnt%3==0:
                    remove-=1
                    replace-=1
                elif cnt%3==1:
                    rm2+=1
            if idx<L:
                pre=password[idx]
                cnt=1
                idx+=1

        use2=min(rm2,replace,remove//2)
        replace-=use2
        remove-=use2*2
        use3=min(replace,remove//3)
        replace-=use3
        return (L-20) + max(replace,3-categories)

        
        
# @lc code=end

assert Solution().strongPasswordChecker('1234567890123456Baaaaa')==3
assert Solution().strongPasswordChecker('ABABABABABABABABABAB1')==2
assert Solution().strongPasswordChecker('a')==5
assert Solution().strongPasswordChecker('aA1')==3
assert Solution().strongPasswordChecker('1337C0d3')==0