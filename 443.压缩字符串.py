#
# @lc app=leetcode.cn id=443 lang=python3
#
# [443] 压缩字符串
#
from typing import List
# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        ret=0
        pre=chars[0]
        cnt=1
        pos=0
        L=len(chars)
        idx=1
        while idx<L:
            if chars[idx]==pre:
                cnt+=1
            else:
                chars[pos]=pre
                pos+=1
                if cnt>1:
                    for d in str(cnt):
                        chars[pos]=d
                        pos+=1
                pre=chars[idx]
                cnt=1
            idx+=1
        chars[pos]=pre
        pos+=1
        if cnt>1:
            for d in str(cnt):
                chars[pos]=d
                pos+=1
        return pos
# @lc code=end
assert Solution().compress(["a","a","b","b","c","c","c"])==6
assert Solution().compress(["a"])==1
assert Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])==4
