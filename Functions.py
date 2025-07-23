# def square(number):
#     print(number ** 3)

# result= square(3)
# print(result)



# def add(num1, num2):
#     return num1 + num2

# print(add(5, 5))



# def multiply(p1,p2):
#     return p1 * p2

# print(multiply(5, 5))
# print(multiply('a', 5))
# print(multiply(5, 'a'))



# import math
# def circle(radius):
#     area = math.pi * radius ** 2
#     circumference = 2 * math.pi * radius
#     return area, circumference

# print(circle(3))



# def greet(name):
#     return "Hello, " + name +"!"
# print(greet("Alice"))



# cube= lambda x: x ** 3
# print(cube(3))



# def sum_all(*args):
#     return sum(args)

# print(sum_all(1, 2, 3, 4, 5))




# def print_kwargs(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")

# print_kwargs(name="Hulk", power="Super Strength" )




# def even_generator(limit):
#     for num in range(2, limit + 1, 2):
#         yield num

# for num in even_generator(10):
#     print(num)




def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))


    
