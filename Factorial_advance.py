n = int(input("Enter a number of which you want to calculate factorial of : "))
answer = 1 
if (n<0):
    print("Not defined")
else: 
    while (n > 0):
        answer=answer*n
        n = n- 1
    print (answer)

