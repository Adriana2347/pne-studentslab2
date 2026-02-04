def fibosum(k):
    a, b = 0, 1
    count = a+b
    for i in range(k-1):
        a, b = b, a + b
        count += b
    return count

n = int(input("Enter a number of series you want: "))
function = fibosum(n)
print(function)
