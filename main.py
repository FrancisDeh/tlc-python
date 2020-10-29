# Introducing Python
# Question 2
# value = int(input("Enter a number: "))
# if value % 2 == 0:
#     print(value, " is Even")
# else:
#     print(value, "is Odd")

# Question 3
# age = 56
# name = "James Bond"
# print("Age ", )

total = 0
for age in range(1, 25):
    total += age
print(total, " years")
print(type(5))

from decimal import *

print(Decimal(".1") + Decimal(".1") + Decimal(".1"))

list1 = [1, 4, 9, 16, 25]
odd_list = [value for value in list1 if value % 2 != 0]
print(odd_list)

name = "Francis Deh"
print(name[-1])


def variable(value_list, *kwargs):
    print(value_list)
    print(kwargs)

    index_list = []
    for index in range(0, len(kwargs)):
        index_list.append(kwargs[index])

    print(index_list)
    values = []
    for value in index_list:
        values.append(value_list[value])

    return tuple(values)


numbers = variable([value for value in range(1, 30)], 3, 5, 6, 7, 0)
print(numbers)
