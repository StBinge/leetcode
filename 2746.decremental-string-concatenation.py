#
# @lc app=leetcode.cn id=2746 lang=python3
# @lcpr version=30204
#
# [2746] 字符串连接删减字母
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        f={}
        w0=words[0]
        f[w0[0]+w0[-1]]=len(w0)
        for i in range(1,len(words)):
            ch=words[i]
            s,e,l=ch[0],ch[-1],len(ch)
            _f=defaultdict(lambda: float('inf'))
            for key,val in f.items():
                ss,ee=key
                s_ee=s+ee
                _f[s_ee]=min(_f[s_ee],l+val-(e==ss))
                ss_e=ss+e
                _f[ss_e]=min(_f[ss_e],l+val-(ee==s))
            f=_f
        return min(f.values())


# @lc code=end
assert Solution().minimizeConcatenatedLength(["a","cba","a"]) == 3
assert Solution().minimizeConcatenatedLength(["ici","i","eceah","de","af","dieb","jb","hcafc","dfe","jgdfg","iihga","bfd","e","geai","bh","d","fia","ebgag","i","eef","b","hijc","jhf","cc"]) == 63
assert Solution().minimizeConcatenatedLength(["aaa", "c", "aba"]) == 6
assert Solution().minimizeConcatenatedLength(["ab", "b"]) == 2
assert Solution().minimizeConcatenatedLength(["aa", "ab", "bc"]) == 4


#
# @lcpr case=start
# ["aa","ab","bc"]\n
# @lcpr case=end

# @lcpr case=start
# ["ab","b"]\n
# @lcpr case=end

# @lcpr case=start
# ["aaa","c","aba"]\n
# @lcpr case=end

#
