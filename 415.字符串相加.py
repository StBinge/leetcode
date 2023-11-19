#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        N1,N2=len(num1),len(num2)
        i1,i2=N1-1,N2-1
        ord0=ord('0')
        ret=[0]*(max(N1,N2)+1)
        idx=0
        carry=0
        while i1>=0 or i2>=0 or carry:
            d1=0
            if i1>=0:
                d1=ord(num1[i1])-ord0
                i1-=1
            d2=0
            if i2>=0:
                d2=ord(num2[i2])-ord0
                i2-=1
            s=d1+d2+carry
            if s>9:
                s%=10
                carry=1
            else:
                carry=0
            ret[idx]=s
            idx+=1
        # if carry:
        #     ret[idx]=1
        #     idx+=1
        return ''.join([str(d) for d in reversed(ret[:idx])])
# @lc code=end

print(Solution().addStrings('11','123'))
print(Solution().addStrings('456','77'))
print(Solution().addStrings('0','0'))