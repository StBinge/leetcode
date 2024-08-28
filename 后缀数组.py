def get_sa_by_sort(s: str):
    N = len(s)
    sa = [0] * (N << 1)
    rk = [0] * (N << 1)

    orda = ord("a")
    for i in range(N):
        sa[i] = i
        rk[i] = ord(s[i]) - orda + 1

    w = 1
    while w < N:
        sa[:N] = sorted(sa[:N], key=lambda idx: rk[idx] * 26 + rk[idx + w])
        _rk = rk.copy()
        p = 0
        rk[sa[0]] = p
        for i in range(1, N):
            if _rk[sa[i]] == _rk[sa[i - 1]] and _rk[sa[i] + w] == _rk[sa[i - 1] + w]:
                rk[sa[i]] = p
            else:
                p += 1
                rk[sa[i]] = p
        w <<= 1
    return sa[:N]


def get_sa_by_counting_sort(s: str):
    N = len(s)
    sa = [0] * N
    rk = [0] * (N << 1)
    cnt = [0] * 28
    for i in range(N):
        code = ord(s[i]) - ord("a") + 1
        rk[i] = code
        cnt[code + 1] += 1

    for i in range(1, 27):
        cnt[i] += cnt[i - 1]

    for i in range(N):
        code = rk[i]
        sa[cnt[code]] = i
        cnt[code] += 1

    p = 1
    oldrk = rk.copy()
    rk[sa[0]] = p
    for i in range(1, N):
        if oldrk[sa[i]] != oldrk[sa[i - 1]]:
            p += 1
        rk[sa[i]] = p

    w = 1
    while w < N:
        # 第二关键字排序
        # cnt=[0]*(p+2)
        # for i in range(N):
        #     cnt[rk[i+w]+1]+=1

        # for i in range(1,p+2):
        #     cnt[i]+=cnt[i-1]

        # id=sa.copy()
        # for i in range(N):
        #     code=rk[id[i]+w]
        #     sa[cnt[code]]=id[i]
        #     cnt[code]+=1

        # 第二关键字优化排序
        id = [0] * N
        cur = 0
        for i in range(N - w, N):
            id[cur] = i
            cur += 1
        for i in range(N):
            if sa[i] >= w:
                id[cur] = sa[i] - w
                cur += 1
        sa = id

        # 第一关键字排序
        cnt = [0] * (p + 2)
        for i in range(N):
            cnt[rk[i] + 1] += 1

        for i in range(1, p + 2):
            cnt[i] += cnt[i - 1]

        id = sa.copy()
        for i in range(N):
            code = rk[id[i]]
            sa[cnt[code]] = id[i]
            cnt[code] += 1

        oldrk = rk.copy()
        p = 1
        rk[sa[0]] = p
        for i in range(1, N):
            if (
                oldrk[sa[i]] != oldrk[sa[i - 1]]
                or oldrk[sa[i] + w] != oldrk[sa[i - 1] + w]
            ):
                p += 1
            rk[sa[i]] = p

        w <<= 1

    return sa


def make_test_str(n: int):
    ret = ""
    orda = ord("a")
    ordz = ord("z")
    for i in range(n):
        ret += chr(random.randint(orda, ordz))
    return ret


def test_sa(s, sa_maker):
    n = len(s)
    ss = []
    for i in range(n):
        ss.append(s[i:])
    ss.sort()
    sa = sa_maker(s)
    sas = []
    for i in range(n):
        sas.append(s[sa[i] :])
    idx = 1

    for x, y in zip(ss, sas):
        idx += 1
        line = f"{str(idx).rjust(4)}\t{x.ljust(n)}\t{y.ljust(n)}"
        print(line)
    assert ss == sas


def tester(sa_maker):
    test_str = "aabaaaab"
    test_sa(test_str, get_sa_by_counting_sort)


if __name__ == "__main__":
    import random

    for i in range(10, 20):
        s = make_test_str(i)
        test_sa(s, get_sa_by_counting_sort)
