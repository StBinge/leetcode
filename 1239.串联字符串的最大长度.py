#
# @lc app=leetcode.cn id=1239 lang=python3
#
# [1239] 串联字符串的最大长度
#
from sbw import *
# @lc code=start
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks=[0]
        orda=ord('a')
        ret=0
        for s in arr:
            mask=0
            for c in s:
                bit=1<<(ord(c)-orda)
                if mask & bit:
                    break
                mask|=bit
            else:
                for i in range(len(masks)):
                    m=masks[i]
                    if m & mask:
                        continue
                    combine=m|mask
                    masks.append(combine)
                    ret=max(ret,combine.bit_count())
                masks.append(mask)
        return ret

# @lc code=end
assert Solution().maxLength(["aa","bb"])==0
assert Solution().maxLength(["cha","r","act","ers"])==6
assert Solution().maxLength(["un","iq","ue"])==4
