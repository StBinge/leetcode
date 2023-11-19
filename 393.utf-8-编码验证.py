#
# @lc app=leetcode.cn id=393 lang=python3
#
# [393] UTF-8 编码验证
#
from typing import List
# @lc code=start
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        cnt=0
        for num in data:
            if cnt>0:
                if num>>6!=2:
                    return False
                cnt-=1
                continue
            if num <128:
                continue

            mask=1<<7
            while mask>1 and  num & mask==mask:
                cnt+=1
                mask>>=1
            cnt-=1
            if not 0<cnt<4:
                return False
        return cnt==0
# @lc code=end

assert Solution().validUtf8([248,130,130,130])==False
assert Solution().validUtf8([145])==False
assert Solution().validUtf8([230,136,145])
assert Solution().validUtf8([255])==False
assert Solution().validUtf8([197,130,1])
assert Solution().validUtf8([235,140,4])==False