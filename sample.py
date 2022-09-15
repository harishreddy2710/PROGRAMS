
# 1)Write a program to calculate the length of a string.
# st = "Harish"
# print(st)
# print(len(st))

# 2)Write a program to convert a string which is a number in nature into integer and Float.
# x = input("enter a number : ")
# y = print(int(x))
# z = print(float(x))

# 3)Write a program that demonstrates the typecasting for dictionary
# tup = (('a', 1),("b", 2))
# print(tup)
# print(type(tup))
# c = dict(tup)
# print(c)
# print(type(c))

# 4)Write a program that converts a list to tuple and vise versa.
# lst = [1,2,3,4,5,6,7,8,9,10]
# print(lst)
# tup = tuple(lst)
# print(tup)
# print(type(tup))
# lst = list(tup)
# print(lst)
# print(type(lst))

# 5)Write a program to update the values of some keys in a dictionary.
# d1 = {'a':1, 'b': 2, 'c': 3}
# d2 = {'a': 200, 'b':3000, 'c':40000}
# print(d1)
# print(d2)
# d1.update(d2)
# print(d1)

# 6)Write a program to demonstrate the differences between list and tuple.
# lst = [12,131,145,56,786,9098]
# print(lst)
# lst[1] = [454]
# print(lst)
#
# tup = (12,323,43,54,45,65,464,5)
# print(tup)
# tup[5] = (9) # throws an error because it is immutable TypeError: 'tuple' object does not support item assignment
# print(tup)

# 7)Write a program to get the following output.
# s = 'Welcome to python'
# x= s [4:10]
# print(x)
# #
# 8)Print the following string in reverse order.
# st = 'HARISH'
# k = st[::-1]
# print(k)

# 9)Write a program to get the following output
# lst= [10, 5, 4, 20, 1, 15, 12]
# # Output: [1, 4, 5, 10, 12, 15, 20]
# lst.sort()
# print(lst)

# 10)Write a program to demonstrate list and dictionary comprehension.
# lst = [i for i in range(20) if i % 2 == 0]
# print(lst)
#
# my_dict= {x : x**2 for x in [1,2,3,4,5]}
# print(my_dict)

# 11)Write a program to reverse a string word by word.

# s = 'a program to reverse a string word by word'
# k = s.split()[::-1]
# print(k)



# 12)Write a program to get the list of even numbers from a given list using list comprehension.
# lst = range(20)
# num = [x for x in lst if x%2==0]
# print(num)

# 13)Write a program to create a dictionary using two lists
# Input: l1 = ['a', 'b', 'c']
# l2 = [1,2,3]
# Output:
# {'a': 1, 'b': 2, 'c': 3}
# l1 = ['a', 'b', 'c']
# l2 = [1,2,3]
# l3 = zip(l1,l2)
# print(dict(l3))


# 14)Write a program to generate and print a list of the first and last 5 elements where the values
# are square of numbers between 1 and 30 (both included).
# lst = range(1,31)
# lst1 = []
# for i in lst:
#     lst1.append(i*i)
#
# print(lst1)
# lst2 = lst1[:5]
# print(lst2)
# lst3 = lst1[-5:]
# print(lst3)

# 15)Define index, number, and compare that the number exists in the list for a given index or not?

# 16)Write a program to find the list of words that are longer than n from a given list of words.
#
# def long_w(n , str):
#     word_lo = []
#     txt = str.split(" ")
#     for x in txt:
#         if len(x)>n:
#             word_lo.append(x)
#     return word_lo
# print(long_w(3,"index, number, and compare that the number exists in the list for a given index or not"))


# 17)Write a Python script to concatenate following dictionaries to create a new one

# Input:
# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dic3 = {5:50,6:60}
#
# dic4 = { }
# for d in dic1,dic2,dic3: dic4.update(d)
#
# print(dic4)
# output:
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


# 18)Write a program to demonstrate all the available operators in python.
# x,y = [30 , 40]
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x//y)
# print(x % y)



# 19)Write a program to get unique values from a list.
# lst = [10,20,30,40,30,50,60,70]
# st = set(lst)
# lst1 = list(st)
# print(lst1)git



# 20)Write a program to update the value in a dictionary if the key exists.
