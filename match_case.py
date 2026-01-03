# this is called match case 
# it was introduced in python 3.10 
# it is similar to switch statement

'''

num = int(input("enter a number"))

match num:
    case 1:
        print("congrats you won 10$");
    case 2:
        print("you have won 100$");
    case 3:
        print("you have won 10000$");
    case _:
        print("better luck next time")

        '''

# loops

#for loop

# for i in range(1,6):
#     print(i)

# for i in range(1,11):
#     print("5 X",i,"=",5*i)

# fruits = ["apple","banana","pineapple","mango"]

# for fruit in fruits:
#     print(fruit)


# while loop

# i=1
# while i<6:
#     print(i)
#     i=i+1

# break statement

for i in range(20):
    if i==10:
        break
    print(i)

    #continue statement

for i in range(20):
    if i==10:
        continue
    print(i)

#pass statement 

for i in range(5):
    if i == 3:
        pass # Do nothing
        print(i) 