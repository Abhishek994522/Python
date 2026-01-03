# num = int(input("Enter a number"))
# if(num>0):
#     print("this is positive number")
# elif(num==0):
#     print("this number is zero")
# else:
#     print("this is a negative number")



# age = int(input("Enter your age"))
# if(age>=18):
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")



# number = int(input("enter a number"))
# if(number%2==0):
#     print("Even")
# else:
#     print("Odd")






# day = int(input("Enter a Day number"))

# match day:
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Teusday")
#     case 4:
#         print("Wednesday")
#     case 5:
#         print("Thursday")
#     case 6:
#         print("Friday")
#     case 7:
#         print("Saturday")
#     case _:
#         print("Invalid day")





# num1 = int(input("enter num1"))
# num2 = int(input("enter num2"))
# operation = input("enter operation(+,-,*,/):")
# match operation:
#     case "+":
#         print(num1+num2)
#     case "-":
#         print(num1-num2)
#     case "*":
#         print(num1*num2)
#     case "/":
#         print(num1/num2)
#     case "mod":
#         print(num1%num2)
#     case _:
#         print("Invalid day")




#for loops

# for i in range(11):
#     print(i)


# num = int(input("enter a number"))
# for i in range(1,11):
#     print(num,"X",i,"=",i*num)

#n(n+1)/2


# n = 100
# for i in range(n):
#     sum=n*(n+1)/2
#     print(sum)

# total=0
# for i in range(1,101):
#     total +=i
#     print(total)


# for i in range(1,5):
#     print("*" * i)





# While loop

# num = 1
# while num<11:
#     print(num)
#     num += 1


# correct_password = "abc123"

# while True:
#     enter_password = input("enter a password")
#     if(enter_password==correct_password):
#         print("Access Granted")
#         break
#     else:
#         print("Incorrct Password")




# Reverse a number using while loop

# num = int(input("Enter a number: "))
# reversed_num = 0

# while num > 0:
#     digit = num % 10              # Get the last digit
#     reversed_num = reversed_num * 10 + digit  # Append digit to reversed number
#     num = num // 10               # Remove the last digit

# print("Reversed number:", reversed_num)



# for i in range(1,10):
#     if i==5:
#         break
#     print(i)

# for i in range(1,10):
#     if i==5:
#         continue
#     print(i)

for i in range(1,5):
    if i==3:
        pass
    print(i)