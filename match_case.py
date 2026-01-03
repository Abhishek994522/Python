# this is called match case 
# it was introduced in python 3.10 
# it is similar to switch statement

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