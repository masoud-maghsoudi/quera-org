#This code written for solving https://quera.ir/problemset/129726/
def separator(ls):
    even, odd = [], []
    for i in ls:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return tuple([even, odd])