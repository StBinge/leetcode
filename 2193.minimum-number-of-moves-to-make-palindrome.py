#
# @lc app=leetcode.cn id=2193 lang=python3
# @lcpr version=30204
#
# [2193] 得到回文串的最少操作次数
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Tree:
    def __init__(self, n) -> None:
        self.vals = [0] * (n + 1)
        self.n = n

    def lowbit(self, idx):
        return idx & -idx

    def add(self, idx, val):
        while idx <= self.n:
            self.vals[idx] += val
            idx += self.lowbit(idx)

    def query(self, idx):
        ret = 0
        while idx:
            ret += self.vals[idx]
            idx -= self.lowbit(idx)
        return ret


class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        N = len(s)
        used = [False] * N
        pos = defaultdict(list)
        mid_code = 0
        for i, ch in enumerate(s):
            pos[ch].append(i)
            mid_code ^= ord(ch)
        ret = 0
        offset = 0
        cnt = N // 2
        idx = 0
        tree = Tree(N)
        mid_idx = -1
        if mid_code:
            mid_ch = chr(mid_code)
            mid_cnt = len(pos[mid_ch])
            mid_idx = pos[mid_ch][mid_cnt // 2]
        while cnt:
            while used[idx]:
                idx += 1
            if idx == mid_idx:
                # ret+=N//2-offset
                # tree.add(idx+2,-1)
                # tree.add(N//2+2,+1)
                # mid=offset
                ret += N // 2 - offset
                idx += 1
                continue
            right = pos[s[idx]].pop()
            used[right] = True
            _right = right + tree.query(right + 1)
            ret += N - 1 - offset - _right
            cnt -= 1
            idx += 1
            offset += 1
            tree.add(right + 1, -1)

        return ret


# @lc code=end


assert Solution().minMovesToMakePalindrome("scpcyxprxxsjyjrww") == 42
assert Solution().minMovesToMakePalindrome("skwhhaaunskegmdtutlgtteunmuuludii") == 163
assert Solution().minMovesToMakePalindrome("eqvvhtcsaaqtqesvvqch") == 17
assert Solution().minMovesToMakePalindrome("letelt") == 2
assert Solution().minMovesToMakePalindrome("aabb") == 2

#
# @lcpr case=start
# "aabb"\n
# @lcpr case=end

# @lcpr case=start
# "letelt"\n
# @lcpr case=end

#
