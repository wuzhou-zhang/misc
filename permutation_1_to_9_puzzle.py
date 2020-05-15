from itertools import permutations

#     a b
#  x    c
# _________
#     d e
#  +  f g
# _________
#     h i

print len(list(permutations(range(1, 10))))
for permutation in permutations(range(1, 10)):
    a, b, c, d, e, f, g, h, i = permutation
    if (10 * a + b) * c != 10 * d + e:
        continue
    if (10 * d + e) + (10 * f + g) != 10 * h + i:
        continue
    print 'answer is:', permutation

#     1 7
#  x    4
# _________
#     6 8
#  +  2 5
# _________
#     9 3
