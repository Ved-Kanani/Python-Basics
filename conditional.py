# age = 13  

# if age<13:
#     print("child")
# elif age<20:
#     print("teenager")
# elif age<60:
#     print("adult")
# else:
#     print("senior citizen")



# age = 26
# day = "sunday"

# price = 12 if age >= 18 else 8

# if day == "wednesday":
#     price = price - 2

# print("ticeket price for you is", price)



# score = 85
# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:   
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "FAIL"

# print("Your grade is", grade)



# fruit = "apple"
# color = "red"
# if fruit == "apple":
#     if color == "green":
#         print("fruit is not ripe.")

#     elif color == "red":
#         print("ready to eat.")

#     elif color == "dark red":
#         print("overripe.") 
#     else:
#         print("unknown color.")



# weather = "sunny"
# if weather == "sunny":
#     print("Go for a walk.")

# elif weather == "rainy":
#     print("Read a book.")

# elif weather == "snowy":
#     print("Build a snowman.")
# else:
#     print("Stay indoors and relax.")



# distance = 150
# if distance < 3:
#     print("walk")

# elif distance <= 15 :
#     print("bike")

# else:
#     print("car")



# size = "small"
# extra_cheese = True

# if extra_cheese:
#     pizza = size + " pizza with extra cheese"

# else:  
#     pizza = size + " pizza without extra cheese"

# print("Your order is:", pizza)



# password = input("Enter your password: ")
# print("your password is:", password)

# if len(password) < 6:
#     strength = "weak"

# elif len(password) <= 10:
#     strength = "medium"

# else:
#     strength = "strong"

# print("your password strength is :", strength)



year = input("Enter a year: ")
print(year)

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.") 