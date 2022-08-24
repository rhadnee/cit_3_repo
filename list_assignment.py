# #number 1


# num = int(input("Enter a list size: "))
# divisible_five = [i for i in range(num) if i%5 == 0 ]
# print (divisible_five)
# print (sum(divisible_five))

#number 2

# nouns = ['abc', 'xyz', 'aba' , '1221', 'amba', 'entre', '37783']

# num = len([a for a in nouns if (len(a)>= 2 and a[-1] == a[0])])
# print (num)

#number 3

# fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]

# for i in fruits:
#     if fruits.count(i) > 1:
#         fruits.remove(i)
#         print(fruits)


# number 4

# hue = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# hue.pop()

# del hue[0:5:4]

# print(hue)

# number 5


# print(squares)

squares = [i*i for i in range (1,6)]
squares.extend([1, 30])
print(squares[5:])




