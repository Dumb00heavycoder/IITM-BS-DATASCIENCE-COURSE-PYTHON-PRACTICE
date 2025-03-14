num = int(input("Enter the number: "))
absstr= str(abs(num))
reverse = " "
for c in absstr:
    reverse = c + reverse
if (num < 0 ):
    reversed = '-'+reverse
if (num == int(reverse)):
    print("PALINDROME")
else: 
    print("NOT PALINDROME")