print("Enter the number")
a = int(input())
if (a%5 == 0 and a%10 == 0):
    print("Last digit is 0")
elif (a%5 == 0 and a%10 != 0):
    print("Last digit is 5")
else: 
    print("last digit is any other")