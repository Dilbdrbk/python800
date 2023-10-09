import random #lambda are also known as anonomys function
random.seed(0)
signal = [random.randint(1,25) for i in range(10)]#list comprehension
print(signal)

#lambda function is used with map(lambda_function, list) and filter(lambda_function, list)
#syntax: lambda arguments: Expression

odd = filter(lambda x: x%2 == 1, signal)
even = filter(lambda x: x%2 == 0, signal)

print(f"the odd number are: {list(odd)}")#list typecast
print(f"the even numbers are: {list(even)}")

squares = map(lambda x: x**2, signal)

print("the squares are:",list(squares))