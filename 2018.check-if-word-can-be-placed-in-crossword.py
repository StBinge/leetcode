#
# @lc app=leetcode.cn id=2018 lang=python3
# @lcpr version=30204
#
# [2018] 判断单词是否能放入填字游戏内
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        N = len(word)

        def check_rows():
            for r in range(R):
                # empty_cnt=0
                cnt1 = 0
                cnt2 = 0
                c = 0
                while c < C and C - c + max(cnt1, cnt2) >= N:
                    if board[r][c] == "#":
                        if cnt1 == N or cnt2 == N:
                            return True
                        cnt1 = cnt2 = 0
                        c += 1
                        continue
                    if max(cnt1, cnt2) == N:
                        while c < C and board[r][c] != "#":
                            c += 1
                        c += 1
                        cnt1 = cnt2 = 0
                        continue
                    if board[r][c] == " ":
                        cnt1 += 1
                        cnt2 += 1
                        c += 1
                    else:
                        if cnt1 != -1:
                            if board[r][c] == word[cnt1]:
                                cnt1 += 1
                            else:
                                cnt1 = -1

                        if cnt2 != -1:
                            if board[r][c] == word[-1 - cnt2]:
                                cnt2 += 1
                            else:
                                cnt2 = -1

                        c += 1

                    if cnt1 == cnt2 == -1:
                        while c < C and board[r][c] != "#":
                            c += 1

                        c += 1
                        cnt1 = cnt2 = 0
                if cnt1 == N or cnt2 == N:
                    return True
            return False

        def check_cols():
            for c in range(C):
                # empty_cnt=0
                cnt1 = 0
                cnt2 = 0
                r = 0
                while r < R and R - r + max(cnt1, cnt2) >= N:
                    if board[r][c] == "#":
                        if cnt1 == N or cnt2 == N:
                            return True
                        cnt1 = cnt2 = 0
                        r += 1
                        continue
                    if max(cnt1, cnt2) == N:
                        while r < R and board[r][c] != "#":
                            r += 1
                        r += 1
                        cnt1 = cnt2 = 0
                        continue
                    if board[r][c] == " ":
                        cnt1 += 1
                        cnt2 += 1
                        r += 1
                    else:
                        if cnt1 != -1:
                            if board[r][c] == word[cnt1]:
                                cnt1 += 1
                            else:
                                cnt1 = -1

                        if cnt2 != -1:
                            if board[r][c] == word[-1 - cnt2]:
                                cnt2 += 1
                            else:
                                cnt2 = -1
                        r += 1
                    if cnt1 == cnt2 == -1:
                        while r < R and board[r][c] != "#":
                            r += 1

                        r += 1
                        cnt1 = cnt2 = 0
                if cnt1 == N or cnt2 == N:
                    return True
            return False

        return (C >= N and check_rows()) or (R >= N and check_cols())


# @lc code=end
assert (
    Solution().placeWordInCrossword(
        board=[["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word="ca"
    )
    == True
)
assert (
    Solution().placeWordInCrossword(
        board=[[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word="ac"
    )
    == False
)
assert Solution().placeWordInCrossword(
    board=[["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word="abc"
)


#
# @lcpr case=start
# [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]]\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]]\n"ac"\n
# @lcpr case=end

# @lcpr case=start
# [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]]\n"ca"\n
# @lcpr case=end

#
