a = 0
b = 1
n_terms = 11

print(a, end=' ')
for i in range(n_terms - 1):
    print(b, end=' ')
    a, b = b, a + b
