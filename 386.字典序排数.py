#
# @lc app=leetcode.cn id=386 lang=python3
#
# [386] 字典序排数
#
from typing import List
# @lc code=start
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # if n<10:
        #     return [i for i in range(1,n+1)]
        # ret=[i for i in range(1,10)]
        # left,right=0,9
        ret=[0]*n
        num=1
        for i in range(n):
            ret[i]=num
            if num*10<=n:
                num*=10
            else:
                while num % 10==9 or num+1>n:
                    num//=10
                num+=1
        return ret
# @lc code=end

print(Solution().lexicalOrder(13))
print(Solution().lexicalOrder(2))