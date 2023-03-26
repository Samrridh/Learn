# m = int(input("Enter the weight in pounds"))
# print(m * 0.45)

# m = "i am samrridh"
# print (m[1:5])

# f = "sam"
# s = "ridh"
# msg = f'{f}{s} is a nice person'
# print(msg)

# password = 'dabvcuavhefuhidbf'
# print (password.upper())

# x=7
# x+=3
# print(x)

# import math
# print( math.ceil(2.9))

########################if statement######################################
# is_hot = False
# is_cold = True

# if is_hot:
#     print("It's a hot day")
    
# elif is_cold:
#     print("wear warm cloths")

# else:
#     print("lovely day")
# print("Enjoy the day")

##########################if statement practise###################################
# is_good = False

# if is_good:
#     print("Put down 10%")
# else:
#     print("Put down 20%")
# print("We hope you have a good day")

########################knwoing the use of len, abs and round######################################

# x = -2.8
# print(abs(round(x)))

###########################using and statement###################################
# good_income = True
# good_credit = True

# if good_credit and good_income:
#     print("Give loan")
# else:
#     print("Do not give loan")

############################using or statement##################################
# good_income = False
# good_credit = True

# if good_credit or good_income:
#     print("Give loan")
# else:
#     print("Do not give loan")

############################using 'and not' and 'or'#######not working###########################
# good_income = False
# good_credit = True
# criminal_record = True

# if good_credit or good_income and not criminal_record:  ## This statement is not working ('or' and 'and not' working together)
#     print("Give loan")
# else:
#     print("Do not give loan")
###########################practising if elif and else###################################

# temp = 9
# if temp >= 30 :
#     print("it's a hot day")
# elif temp <= 10 :
#     print("it's a cold day")
# else:
#     print("neither hot nor a cold day")
##########################using len as password cheker####################################

# name_count = "fh"
# if (len(name_count)) < 3 :
#     print("Minimum 3 characters")
# elif  (len(name_count)) > 50 :
#     print("Maximum 50 characters")
# else:
#     print(" Perfecto password")
###########################using while statement###################################
# s = 2
# while s<= 10:
#      s+=1
#      print("#" * s)   
# print("Done")

##############################using for statement################################

# prices = [10,20,30,40]

# total = 0
# for i in prices :
#     total += i
# print(f"total: {total}")

#######################using for statement to create co-ordiantes#######################

# for x in range (4):
#     for y in range (3):
#         print(f"( {x},{y})")

##########################learning lists####################################

# names = ['fvkbk','khbv','hbv']
# names[0] = "Sam"
# print(names[0:3])

#########################2D lists######################################
# its just a matrix, not practising it

###################Lists method#####################################
# numbers = [1,53,64,24,79,64]
# numbers.append(5) # adds the value at last
# numbers.insert(1,6) # inserts the value at the desired place
# numbers.remove(53) # removes certain value from the lists
# print (numbers) 
# print (numbers.index(24)) # tells the place of that value
# print(24 in numbers) #  boolean value if the number exists or not
# print(numbers.count(64)) # tells the number of time that value has been repeated
# numbers.sort() 
# numbers.reverse()
# print(numbers)


########################Tuples#######################################
# # just use () instead of [] in tuples, tuples can not be edited like lists
# numbers = (2,3,4,665,762)
# print(numbers[0]) # Dont use () while calling a tuple

###########################Unpacking####################################
# values = (1,2,3) 
# x = values[0]
# y = values[1]
# z = values[2]
# #  #this long code is same as 
# x,y,z = values
# print(x)
# # you can use unpacking with lists too

############################Dictionaries###################################
# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "verified": True
# }
# customer["name"] = "Jake"
# print(customer["name"])

#######################Learning Functions########################################
# name = input("whats your name: ")
# def greet_user():
#     print(f"Hi there {name}")
#     print("Hope you have a nice day")
    

# greet_user()

######################Parameters#########################################
# def greet_user(first_name, last_name):
#     print(f"Hi there {first_name} {last_name}")
#     print("Hope you have a nice day")
    

# greet_user("Sam", "organ") 
# greet_user("mas" ,"nagro") # these are positional arguments
# greet_user(last_name="organ", first_name="Sam") # these are keyword arguments
# # they are just like functions just add up an parameter and an argument in the ()

########################Returning values####################################
# def square(num):
#     return num * num
    

# print(square(3))

##################Exceptions##########################################
# try:
#     age = int(input("what's your age"))
#     print(age)
# except ValueError: # you may see the error name in terminal and write an exception for that
#     print("Invalid input")

#################Comments##########lol, already using it#######################
#Though sky is everything except blue but we say thay
# print("sky is blue")

############################Classes and constructors###################################
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
    
#     def move(self):
#         print("move")
        
#     def draw(self):
#         print("draw")


# point = Point(10,20)
# print(point.y)

############################inheritance###################################
# class Mammals:
#     def walk(self):
#         print("walk")


# class Dog(Mammals):
#     def bark(self):
#         print("bark")


# class Cat(Mammals):
#     pass

# dog1 = Dog()
# dog1.bark()

# cat1= Cat()
# cat1.walk()

########################modules(conversion)#######################################

# import conversion
# from conversion import lbs_to_kg

# lbs_to_kg(100)
# # print(conversion.lbs_to_kg(70))

###########################Packages####################################
# # from test.shipping import calc_shipping 
# from test import shipping

# print(shopping.calc_shipping())

###############################################################
# from pathlib import Path


# path = Path("test")
# print(path.exists())

###############################################################





