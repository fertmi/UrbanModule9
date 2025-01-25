from itertools import combinations, chain


def all_variants(text):
    i = 1
    while i!=len(text)+1:
        for j in combinations(text,i):
            yield ''.join(j)
        i += 1

a = all_variants("abc")
for i in a:
    print(i)