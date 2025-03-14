num = int(input("Enter the number: "))
absstr= str(abs(num))
reverse = " "
for c in absstr:
    reverse = c + reverse
if num >= 0:
    print(reverse)
else: 
    print('- ' + reverse)