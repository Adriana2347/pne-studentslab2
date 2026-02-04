
def fibo(k):
    a, b = 0, 1
    for i in range(k - 1):
        a, b = b, a + b
    return b

n = int(input("Enter a number of series you want: "))
func = fibo(n)
print(func)