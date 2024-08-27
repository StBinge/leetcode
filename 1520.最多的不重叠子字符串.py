#
# @lc app=leetcode.cn id=1520 lang=python3
#
# [1520] 最多的不重叠子字符串
#
from sbw import *
# @lc code=start
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        L=len(s)

        first_pos=[-1]*26
        last_pos=[L]*26
        for i,c in enumerate(s):
            idx=ord(c)-ord('a')
            if first_pos[idx]==-1:
                first_pos[idx]=i
            last_pos[idx]=i
        sorted_last_pos=sorted([[i,p] for i,p in enumerate(last_pos) if p<L],key=lambda x:x[1])
        pre_end=-1
        ret=[]
        for code, end in sorted_last_pos:
            start=first_pos[code]
            if start<=pre_end:
                continue
            i=end
            while i>start:
                idx=ord(s[i])-ord('a')
                left=first_pos[idx]
                start=min(left,start)
                if start<=pre_end:
                    break
                right=last_pos[idx]
                if right>end:
                    break
                i-=1
            if i==start:
                ret.append(s[start:end+1])
                pre_end=end
        return ret

# @lc code=end
assert sorted(Solution().maxNumOfSubstrings('abbaccd'))==sorted(["d","bb","cc"])
assert sorted(Solution().maxNumOfSubstrings('abab'))==sorted(['abab'])
assert sorted(Solution().maxNumOfSubstrings('adefaddaccc'))==sorted(["e","f","ccc"])
