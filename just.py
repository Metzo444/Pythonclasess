# rows = int(input("Enter number of rows: "))

# k = 0

# for i in range(1, rows + 1):
#     for space in range(1, (rows - i) + 1):
#         print(end="  ")

#     while k != (2 * i - 1):
#         print("* ", end="")
#         k += 1

#     k = 0
#     print(end="")
#     rows = int(input("Enter number of rows: "))

#     for i in range(rows, 1, -1):
#         for space in range(0, rows - i):
#             print("  ", end="")
#         for j in range(i, 2 * i - 1):
#             print("* ", end="")
#         for j in range(1, i - 1):
#             print("* ", end="")
#         print()
#
# order_1 = int(input("Choose the dishes : 1 is Pizza with cheese(2000),2:Pizza with mashroom(2300):\n"))
# order_2 = int(input("Choose the dishes : 1 is Mayonez(300),2:Ketchup(350):\n"))
#
# Pizza_with_cheese = 2000
# Pizza_with_mashroom = 2300
# Mayonez = 300
# Ketchup = 350
#
# print(("You ordered Pizza_with_cheese and Mayonez " + str(Pizza_with_cheese + Mayonez))*(order_1 == 1 and order_2 == 1 ),end="")
# print(("You ordered Pizza_with_cheese and Ketchup " + str(Pizza_with_cheese + Ketchup))*(order_1 == 1 and order_2 == 2 ),end="")
# print(("You ordered Pizza_with_mashroom and Mayonez " + str(Pizza_with_mashroom + Mayonez))*(order_1 == 2 and order_2 == 1 ),end="")
# print(("You ordered Pizza_with_mashroom and Ketchup " + str(Pizza_with_mashroom + Ketchup))*(order_1 == 2 and order_2 == 2 ),end="")
#
def even_num_gen(a):
    for i in range(a+1):
        if i % 2 ==0:
            yield i
gen2 = even_num_gen(100)
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))


import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
all = lower + upper + numbers

length = 8
password = "".join(random.sample(all,length))
print(f"Your random password is {password}")

