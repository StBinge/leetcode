#
# @lc app=leetcode.cn id=1363 lang=python3
#
# [1363] 形成三的最大倍数
#
from sbw import *
# @lc code=start
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
 
        counter=[0]*10
        s=0
        mods=[0]*3
        for d in digits:
            counter[d]+=1
            s+=d
            mods[d%3]+=1
        mod1=[1,4,7]
        mod2=[2,5,8]
        excess=s%3
        remove_mod,cnt=0,0
        if excess==1:
            remove_mod,cnt=(1,1) if mods[1]>0 else (2,2)
        elif excess==2:
            remove_mod,cnt=(2,1) if mods[2]>0 else (1,2)
        
        if remove_mod:
            for i in (mod1 if remove_mod==1 else mod2):
                dif=min(counter[i],cnt)
                counter[i]-=dif
                cnt-=dif
                if cnt==0:
                    break
        
        ret=''
        for i in range(9,0,-1):
            ret+=str(i)*counter[i]
        if ret:
            ret+='0'*counter[0]
        else:
            ret+='0'*min(1,counter[0])
        return ret



# @lc code=end

assert Solution().largestMultipleOfThree([8,7,0,7,7])=='7770'
assert Solution().largestMultipleOfThree([0,0,0,0,0,0])=='0'
assert Solution().largestMultipleOfThree([1])==''
assert Solution().largestMultipleOfThree([8,6,7,1,0])=='8760'
assert Solution().largestMultipleOfThree([8,1,9])=='981'