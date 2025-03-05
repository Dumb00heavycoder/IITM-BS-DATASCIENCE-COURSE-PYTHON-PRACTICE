num = int(input("Enter a number: "))
absnum = abs(num)
rev = absnum % 10 #rev value becomes  the last digit of the given number
absnum = absnum // 10 #absnum value changes to a number containing the digits except the last digit of absnum
while (absnum>0):
    r = absnum % 10 #r value becomes the last digit of  absnum (updated value of absnum)
    absnum = absnum // 10 #again updation
    rev = rev * 10 + r #stores the value of digits in rev one by one
if (num>0):
    print(rev)
else: 
    print (rev - 2*rev) #anything subtracted by its double will return the negative value of the same number