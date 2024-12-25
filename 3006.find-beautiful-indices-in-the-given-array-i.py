#
# @lc app=leetcode.cn id=3006 lang=python3
# @lcpr version=30204
#
# [3006] 找出数组中的美丽下标 I
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def next(pat: str):
            N = len(pat)
            nxt = [0] * N
            j = 0
            for i in range(1, N):
                while j > 0 and pat[j] != pat[i]:
                    j = nxt[j - 1]
                if pat[j] == pat[i]:
                    j += 1
                nxt[i] = j
            return nxt

        a_nxt = next(a)
        b_nxt = next(b)

        def get_matched(s, pat):
            nxt = next(pat)
            matched = []
            j = 0
            N = len(pat)
            for i, ch in enumerate(s):
                while j > 0 and ch != pat[j]:
                    j = nxt[j - 1]
                if pat[j] == ch:
                    j += 1
                if j == N:
                    matched.append(i - N + 1)
                    j = nxt[j-1]
            return matched

        a_matched = get_matched(s, a)
        b_matched = get_matched(s, b)
        if not b_matched:
            return []
        sn = len(s)
        bn = len(b)
        ret = []
        # l=0
        # r=len(b_matched)-1
        l = 0
        r = 0
        for i in a_matched:
            left = max(i - k, 0)
            l = bisect_left(b_matched, left, lo=l)
            right = min(i + k, sn - bn)
            r = bisect_right(b_matched, right, lo=r)
            if l < r:
                ret.append(i)
        return ret


# @lc code=end
assert Solution().beautifulIndices("ababababazzabababb","aba","bb",10) == [6,11,13]
assert Solution().beautifulIndices("bavgoc","ba","c",6) == [0]
assert Solution().beautifulIndices("frkxslnnn", "rkxsl", "n", 2) == []
assert Solution().beautifulIndices(s="abcd", a="a", b="a", k=4) == [0]
assert Solution().beautifulIndices(
    s="isawsquirrelnearmysquirrelhouseohmy", a="my", b="squirrel", k=15
) == [16, 33]


#
# @lcpr case=start
# "isawsquirrelnearmysquirrelhouseohmy"\n"my"\n"squirrel"\n15\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n"a"\n"a"\n4\n
# @lcpr case=end

#
