def calc_next(p: str | list):
    N = len(p)
    next = [0] * N
    j = 0
    for i in range(1, N):
        while j and p[j] != p[i]:
            j = next[j - 1]
        if p[j] == p[i]:
            j += 1
        next[i] = j
    return next


def match(s: str | list, p: str | list):
    next = calc_next(p)
    m = len(p)
    j = 0
    for i, ch in enumerate(s):
        while j and ch != p[j]:
            j = next[j - 1]
        if ch == p[j]:
            j += 1
        if j == m:
            return i + 1 - m
    return -1


if __name__ == "__main__":
    assert calc_next("abab") == [0, 0, 1, 2]
    assert calc_next("abcabc") == [0, 0, 0, 1, 2, 3]
    assert match("abcabc", "abab") == -1
    assert (r := match("abcabab", "abab")) == 3
    assert (r := match("ababab", "abab")) == 0
