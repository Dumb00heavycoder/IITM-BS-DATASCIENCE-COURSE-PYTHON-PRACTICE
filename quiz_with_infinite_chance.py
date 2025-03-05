print("What is value of pi (till 2 decimal place)?")
answer = float(input())
while(answer != 3.14):
    print("Ah, you got it wrong")
    print("Try again buddy")
    answer = float(input())
print("Well done you got it right")