
#apartado a

def is_even(number):
    if number % 2 == 0:
        result = "True"
    else:
        result = "False"
    return result

number = int(input("Enter a valid number: "))
even = is_even(number)
print(even)

#apartado b

def classification(a, b, c):
    if a == b == c:
        result = "Equilateral"
    elif a == b or a == c or b == c:
        result = "isosceles"
    elif a != b != c:
        result = "scalene"
    return result

a1 = int(input("Enter a valid height: "))
b1 = int(input("Enter a valid height: "))
c1 = int(input("Enter a valid height: "))

print(classification(a1, b1, c1))