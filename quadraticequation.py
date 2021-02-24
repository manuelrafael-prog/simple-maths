import math

a = float(input("Enter the 'a' value? "))
b = float(input("Enter the 'b' value? "))
c = float(input("Enter the 'c' value? "))

sqrt = math.sqrt(abs(b ** 2 - 4 * a * c))

value1 = - b + sqrt / 2 * a
value2 = - b - sqrt / 2 * a

print(value1, "or", value2)
