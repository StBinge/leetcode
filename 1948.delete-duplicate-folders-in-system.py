#
# @lc app=leetcode.cn id=1948 lang=python3
# @lcpr version=30204
#
# [1948] 删除系统中的重复文件夹
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Trie:
    def __init__(self) -> None:
        self.slots = defaultdict(Trie)
        # self.cnt=0
        self.ending = False
        self.expr = ""

    def insert(self, paths: list):
        cur = self
        for path in paths:
            cur = cur.slots[path]
            # cur.cnt+=1
        cur.ending = True


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:

        root = Trie()
        for path in paths:
            root.insert(path)

        counter = defaultdict(int)

        def parse(node: Trie):
            if len(node.slots) == 0:
                return

            sub_exprs = []
            for key in sorted(node.slots.keys()):
                sub = node.slots[key]
                parse(sub)
                sub_exprs.append(f"({key}{sub.expr})")

            node.expr = "".join(sub_exprs)
            counter[node.expr] += 1

        parse(root)

        ret = []

        def find(node: Trie, path: list):
            if node.ending:
                ret.append(path.copy())
            for sub, slot in node.slots.items():
                if counter[slot.expr] > 1:
                    continue
                path.append(sub)
                find(slot, path)
                path.pop()

        find(root, [])
        return ret


# @lc code=end
ret = Solution().deleteDuplicateFolder(
    paths=[["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]
)
ret.sort()
assert ret == sorted([["d"], ["d", "a"]])


#
# @lcpr case=start
# [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]\n
# @lcpr case=end

# @lcpr case=start
# [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]\n
# @lcpr case=end

# @lcpr case=start
# [["a","b"],["c","d"],["c"],["a"]]\n
# @lcpr case=end

# @lcpr case=start
# [["a"],["a","x"],["a","x","y"],["a","z"],["b"],["b","x"],["b","x","y"],["b","z"]]\n
# @lcpr case=end

# @lcpr case=start
# [["a"],["a","x"],["a","x","y"],["a","z"],["b"],["b","x"],["b","x","y"],["b","z"],["b","w"]]\n
# @lcpr case=end

#
