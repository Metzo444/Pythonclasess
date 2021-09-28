#######################################------HomeWorkes------#####################################

### Homework_1------------------------------------------------------------------------------------

# print("name:", "Aram", "\nsurname:", "Azatyan",sep = " ")

# ### Homework_2_a--------------------------------------------------------------------------------

# print("Twinkle, twinkle, little star,", "\tHow I wonder what you are!", "\t\tUp above the world so high,", "\t\tLike a diamond in the sky.", "Twinkle, twinkle, little star,","\tHow I wonder what you are",end = "!", sep = "\n")

# ### Homework_2_b--------------------------------------------------------------------------------

# print("\nHello \n\tPython \n\t\tWorld")

# ### Homework_2_c--------------------------------------------------------------------------------

# ### Homework_3_a--------------------------------------------------------------------------------

# temp = float(input("Enter the temperature:\n"))
# temp1 = temp*1.8+32
# print(f"Now temperature is {temp}°C or {temp1}°F" )

### Homework_3_b----------------------------------------------------------------------------------

# a = 5
# b = 6
# c = 7
# num1 = (a+b+c)/3
# print(num1)   # the average value of a, b, c
# num2 = a**b + b**c
# print(num2)     # a^c + b^c (2^4 in python is 2**4)
# num3 = (a+b)**c
# print(num3)     # (a + b)^c
# num4 = int(str(a)+str(b)+str(c))+a*b*c
# print(num4)  # abc + a*b*c

### Homework_3_c----------------------------------------------------------------------------------

# height = int(input("How tall are you: \n"))
#
# opt_weight = (height**2)*24/10000
# print(f"Your height is {height} cm  and optimal weight for your height is {opt_weight} kg",end = ":")

### Homework_extra--------------------------------------------------------------------------------

# order1 = int(input("\nhello the menu is 1:Pizza(1500), 2 for kebab 750, what you want?\n"))
# order2 = int(input("mayonez(500) or ketchup(100) choose 1 or 2:\n"))
# pizza_price = 1500
# kebab_price = 750
# mayonez_price = 500
# ketchup_price = 100
#
# print(("You ordered pizza with mayonez " + str(pizza_price+mayonez_price))*(order1 == 1 and order2 == 1),end ="" )
# print(("You ordered pizza with ketchup " + str(pizza_price+ketchup_price))*(order1 == 1 and order2 == 2),end ="" )
# print(("You ordered kebab with mayonez " + str(kebab_price+mayonez_price))*(order1 == 2 and order2 == 1),end ="" )
# print(("You ordered kebab with ketchup " + str(kebab_price+ketchup_price))*(order1 == 2 and order2 == 2),end ="" )

### Homework_4_1----------------------------------------------------------------------------------

# distance1 = int(input("\nTell dictance to kilometers:\n"))
# distance = distance1*0.62137119
# print("Your distance is ", distance1, "kilometers or", distance, "miles")

### Homework_4_2----------------------------------------------------------------------------------

# from excgange import dollar_course as dollar, euro_course as euro , pound_course as pound, ruble_course as ruble , yuan_course as yuan
#
# money = float(input("Enter the sum of money:\n"))
#
# in_dollars_to_dram = money * dollar
# in_euros_to_dram = money *  euro
# in_pounds_to_dram = money * pound
# in_rubles_to_dram = money * ruble
# in_yuans_to_dram = money * yuan
#
# print(f"""You have
# {money} dollar that is equal to {in_dollars_to_dram} dram,
# {money} euro that is equal to  {in_euros_to_dram} dram,
# {money} pound that is equal to {in_pounds_to_dram} dram,
# {money} ruble that is equal to {in_rubles_to_dram} dram,
# {money} yuan that is equal to {in_yuans_to_dram} dram: """)

### Homework_4_3----------------------------------------------------------------------------------

# day = int(input("Enter a number 0-6 for days:\n"))
#
# if day == 0:
#     print("Sunday")
# elif day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# else:
#     print("Error 404")

### Homework_4_4----------------------------------------------------------------------------------

# text = input("text something:\n")
# if chr(32) in text:
#     print(True)
# else:
#     print(False)

### Homework_4_5----------------------------------------------------------------------------------

#--first way--#

# num1 = 10
# num2 = 20
# num3 = 30
#
# if num1 > num2 and  num1 > num3:
#     largest = num1
# elif num2 > num1 and num2 > num3:
#     largest = num2
# else:
#     largest = num3
#     print(largest)

#--Second way--#

# num1 = int(input("Enter the number:\n"))
# num2 = int(input("Enter the number:\n"))
# num3 = int(input("Enter the number:\n"))
#
# if num1 > num2 and  num1 > num3:
#     largest = num1
# elif num2 > num1 and num2 > num3:
#     largest = num2
# else:
#     largest = num3
#     print(largest)

### Homework_4_6----------------------------------------------------------------------------------

# year = int(input("Enter the year:\n"))
#
# if year % 4 == 0:
#     print("This year is leap", end=":")
# else:
#     print("This year is not leap",end=":")

### Homework_5_1----------------------------------------------------------------------------------

# string = input("Say something:\n")
# if len(string) < 3:
#     print(string)
# elif string[-3:] == 'ing':
#     print(string + 'ly')
# else:
#     print(string + 'ing')

### Homework_5_2----------------------------------------------------------------------------------

# a = input('Enter a string ')
# b=a
# c=d=0
# c = a.find('not')
# d = a.find('poor')
# e = a.find('good')
# if(c>=0 and d>=0):
#     b = b.replace(b[c:d+4],'good')
# elif  e >= 0:
#     b = b.replace(b[e:e+4],"poor")
# print(b)

### Homework_5_3----------------------------------------------------------------------------------

#-- first way --#

# string = input("Enter the string:\n ")
# string = string[0] + string[1:].replace(string[0],"$")
# print(string)

#-- second way --#

# word = 'restart'
# word1 = word[0]
# word = word.replace(word1, "$")
# word = word1 + word[1:]
# print(word)

### Homework_5_4----------------------------------------------------------------------------------

#numbers = (1,2,3,4,5,6,7,8,9,10,11)
# num14 = int(input("Enter the number:\n"))
# even_number = 0
# odd_number = 0
# for num in range(0,num14):
#     if  num%2:
#         even_number += 1
#     else:
#         odd_number += 1
# print("\nEven number is: ", even_number)
# print("Odd numbers is: ", odd_number)

### Homework_5_5----------------------------------------------------------------------------------
#
# str = input("Enter a string:\n")
# string1 = str[::2]
# print(string1)

### Homework_6_1----------------------------------------------------------------------------------

#--first way--#

# num=5
# for i in range(num):
#     for j in range(i):
#         print ('* ', end="")
#     print('')
#
# for i in range(num,0,-1):
#     for j in range(i):
#         print('* ', end="")
#     print('')

#--Second way--#

# n = int(input("Enter the number:\n"))
# for i in range(n):
# 	for j in range(i):
# 		print("* ",end="")
# 	print('')
#
# for i in range(n,0,-1):
# 	for j in range(i):
# 		print("* ",end="")
# 	print('')

### Homework_6_2----------------------------------------------------------------------------------



### Homework_6_3----------------------------------------------------------------------------------

# x = int(input("Enter the number:\n"))
# for n in range(1,x+1):
#     if x%n == 0:
#         print(f'{n} is the divisor of x')

### Homework_6_4----------------------------------------------------------------------------------

# num = int(input("Enter the number:\n"))
# factorial = 1
#
# # check if the number is negative, positive or zero
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print(f"The factorial of {num} is {factorial}")

### Homework_6_5----------------------------------------------------------------------------------

#--first way--#

# x,y = 0,1
# while y < 50:
#     print(y,end=" ")
#     x,y = y,x+y

#--Second way--#

# x,y=0,1
# num = int(input("\nEnter the num:\n"))
#
# while y < num:
#     print(y,end=" ")
#     x,y = y,x+y

### Homework_7_1----------------------------------------------------------------------------------

# h = float(input("Tell the perpendicular height:\n"))
# b = float(input("Tell the base:\n"))
# def area_of_the_triangle(height,base):
#     area = height*base*1/2
#     print(f"Your triangle's area is equal to {area}")
# area_of_the_triangle(height=h,base=b)

### Homework_7_2----------------------------------------------------------------------------------

def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a = str(input("Enter the string to be reversed: "))
print(reverse(a))

### Homework_7_3----------------------------------------------------------------------------------
#
# word1 = input("Enter the sentence:\n")
# def count_function(word):
#     upper_case = 0
#     lower_case = 0
#     for i in range(len(word)):
#         if ord(word[i])>= 97 and ord(word[i])<= 122:
#             lower_case += 1
#         elif ord(word[i])>= 65 and ord(word[i])<= 90:
#             upper_case +=1
#     print("Upper :", upper_case)
#     print("Lower :", lower_case)
# count_function(word = word1)

### Homework_7_4----------------------------------------------------------------------------------

# axa = input("Text something and see result:\n")
# def isPalindrome(string):
#     left_pos = 0
#     right_pos = len(string) - 1
#
#     while right_pos >= left_pos:
#         if not string[left_pos] == string[right_pos]:
#             return False
#         left_pos += 1
#         right_pos -= 1
#     return True
#
#
# print(isPalindrome(axa))

### Homework_7_5----------------------------------------------------------------------------------

# import random
#
# check_to_play = True
# rounds = 0
# computers_score = 0
# user_score = 0
# while check_to_play:
#     # write the gam
#     user_choice = 'test'
#     # validation of input
#     while user_choice not in ("1","2","3"):
#         user_choice = input("1 for Rock 2 for Paper 3 for Scissors\n")
#     else:
#         user_choice = int(user_choice)
#
#
#     # computer_choice
#     computers_choice = random.randint(1, 3)
#
#     if computers_choice == user_choice:
#         print("Draw")
#     elif (computers_choice == 1 and user_choice == 2) or (computers_choice == 2 and user_choice == 3) \
#             or (computers_choice == 3 and user_choice == 1):
#         print("You Won\U0001F600")
#         user_score += 1
#     else:
#         print('You Lost \U0001F62A')
#         computers_score += 1
#     rounds += 1
#
#     check_input = input("Wanna play again? no for exit\n")
#     if check_input == "no":
#         check_to_play = False
#
# print(f" You have played {rounds} time and the results \n user score - {user_score} and computer score - {computers_score} ")

### Homework_8_1----------------------------------------------------------------------------------



### Homework_8_2----------------------------------------------------------------------------------



### Homework_8_3----------------------------------------------------------------------------------

##--first way--##

# def reverse_v1(x):
#     y = x.split()
#     result = []
#     for word in y:
#         result.insert(0, word)
#     return " ".join(result)
# test1 = input("Enter a sentence:\n")
# print(reverse_v1(test1))


#--Second way--##

# def reverse_v2(x):
#     y = x.split()
#     return " ".join(y[::-1])
# test1 = input("Enter a sentence:\n")
# print(reverse_v2(test1))


##--Third way--##

# def reverse_v3(x):
#     y = x.split()
#     return " ".join(reversed(y))
# test1 = input("Enter a sentence:\n")
# print(reverse_v3(test1))


##--4th way--##

# def reverse_v4(x):
#     y = x.split()
#     y.reverse()
#     return " ".join(y)
# test1 = input("Enter a sentence:\n")
# print(reverse_v4(test1))

### Homework_8_4----------------------------------------------------------------------------------

# # New tuple is created
# def Reverse(tuples):
#     new_tup = tuples[::-1]
#     return new_tup
#
#
# # Driver Code
# tuples = ('z', 'a', 'd', 'f', 'g', 'e', 'e', 'k')
# print(Reverse(tuples))

### Homework_8_5----------------------------------------------------------------------------------

# my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
# new_list = []
#
# while my_list:
#     min = my_list[0]
#     for x in my_list:
#         if x < min:
#             min = x
#     new_list.append(min)
#     my_list.remove(min)
#
# print(new_list)

### Homework_8_6----------------------------------------------------------------------------------

# list1 = [10, 20, 4, 45,74,89,111,55.9,99.99,97,100]
#
# mx = max(list1[0], list1[1])
# secondmax = min(list1[0], list1[1])
# n = len(list1)
# for i in range(2, n):
#     if list1[i] > mx:
#         secondmax = mx
#         mx = list1[i]
#     elif list1[i] > secondmax and \
#             mx != list1[i]:
#         secondmax = list1[i]
#
# print("Second highest number is : ", \
#       str(secondmax))

### Homework_9_1----------------------------------------------------------------------------------
### Homework_9_2----------------------------------------------------------------------------------

# import itertools
# num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# print("Original List", num)
# num.sort()
# new_num = list(num for num,_ in itertools.groupby(num))
# print("New List", new_num)

### Homework_9_3----------------------------------------------------------------------------------

# def flatten_list(n_list):
#     result_list = []
#     if not n_list: return result_list
#     stack = [list(n_list)]
#     while stack:
#         c_num = stack.pop()
#         next = c_num.pop()
#         if c_num: stack.append(c_num)
#         if isinstance(next, list):
#             if next: stack.append(list(next))
#         else: result_list.append(next)
#     result_list.reverse()
#     return result_list
# n_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# print("Original list:")
# print(n_list)
# print("\nFlatten list:")
# print(flatten_list(n_list))

### Homework_9_4----------------------------------------------------------------------------------

# def split_two_parts(n_list, L):
#     return n_list[:L], n_list[L:]
# n_list = [1,1,2,3,4,4,5, 1]
# print("Original list:")
# print(n_list)
# first_list_length = 3
# print("\nLength of the first part of the list:",first_list_length)
# print("\nSplited the said list into two parts:")
# print(split_two_parts(n_list, first_list_length))

### Homework_10_1----------------------------------------------------------------------------------
#
# dict1={1:10,2:20}
# dict2={3:30,4:40}
# dict3={5:50,6:60}
# dict4={6:50,7:60}
# list_dict = [dict1, dict2, dict3, dict4]
# for dict in list_dict:
#     dict3.update(dict)
# print(dict4)


### Homework_10_2----------------------------------------------------------------------------------

# num = int(input("Enter the number:\n"))
# d = {num:num**2 for num in range(1,num+1)}
# print(d)

### Homework_10_3----------------------------------------------------------------------------------

# My_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None}
# print(f"Original dictionary: \n{My_dict} ")
# del(My_dict['c3'])
# print(f"New Dictionary after dropping empty items: \n{My_dict}")

#
# My_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None}
#
# for key, value in  My_dict.copy().items():
#     if not value:
#          My_dict.pop(key)
#
# print(My_dict)

### Homework_10_4----------------------------------------------------------------------------------

# text = input("Enter the sentence:\n")
# def word_count(str):
#     counts = dict()
#     words = str.split()
#
#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
#
#     return counts
#
# print( word_count(text))


### Homework_11_1----------------------------------------------------------------------------------
#
# def even_num_gen(a):
#     for i in range(a+1):
#         if i % 2 ==0:
#             yield i
# gen2 = even_num_gen(100)
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))

### Homework_11_2----------------------------------------------------------------------------------

# import random
#
# lower = "abcdefghijklmnopqrstuvwxyz"
# upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numbers = "0123456789"
# all = lower + upper + numbers
#
# length = 20
# password = "".join(random.sample(all,length))
# print(f"Your random password is {password}")
