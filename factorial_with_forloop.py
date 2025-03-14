n = int(input("Enter the number: "))
answer = 1
if n < 0:
    print("Not defined")
else :
    for i in range(n, 1, -1):
        answer = answer *i
print(answer)