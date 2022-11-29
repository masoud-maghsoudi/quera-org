#This code written for solving https://quera.ir/problemset/129728/
print(" ".join(sorted([x if (ord(x)-97) % 2 == 0 else x.upper() for x in input()], reverse=True)))