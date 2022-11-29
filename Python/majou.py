#This code written for solving https://quera.ir/problemset/276/
def majmou(m, s):
    if m == 1:
        return("{} {}".format(s, s))
    elif s == 0 or s > m*9:
        return("-1 -1")
    s_test_max = s
    s_test_min = s-1
    max = [x*0 for x in range(m)]
    min = [1]
    min.extend([x*0 for x in range(m-1)])

    #Finding Max Value
    ndx = 0
    for i in range(9, 0, -1):
        if s_test_max >= i:
            for j in range(ndx, m):
                max[j] += i
                s_test_max -= i
                ndx += 1
                if s_test_max < i:
                    break
        else:
            continue
    max_str = "".join(list(map(str, max)))
    #Finding Min Value
    ndx = -1
    for i in range(9, 0, -1):
        if s_test_min >= i:
            for j in range(ndx, -m-1, -1):
                min[j] += i
                s_test_min -= i
                ndx -= 1
                if s_test_min < i:
                    break
        else:
            continue
    min_str = "".join(list(map(str, min)))
    return("{} {}".format(min_str, max_str))

if __name__ == "__main__":
    m, s = list(map(int, input().split()))
    print(majmou(m, s))