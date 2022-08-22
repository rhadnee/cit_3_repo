#1 Print first 10 numbers using while loop

i = 1
while i <=10:
    print(i)
    i = i+1




#2 Calculate the sum of all numbers from 1 to 15.
num = 0
total = 0
while num < 10:
    total += num
    num += 1
print(total)





#3 multiplication table of 5 from 1 to 12
n = 5
for i in range(1,13,1):

    product = n*i 
    print (product)

#4 Write a program to display only those numbers from a list that satisfy
# the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next
# number
# If the number is greater than 500, then stop the loop
# given 'numbers = [12, 75, 150, 180, 145, 525, 50]:

decimals = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)


#5. Write a program to count the total number of digits in a number using a while loop. given number '4673453' 

example = 4673453
digit = 0
while num != 0:
    num = num // 10
    digit =digit  + 1
print("Total number of digits are:", digit)




#6. Display numbers from -10 to -1 using while loop

x = -1
while x >= -10:
    print(x)
    x = x - 1
