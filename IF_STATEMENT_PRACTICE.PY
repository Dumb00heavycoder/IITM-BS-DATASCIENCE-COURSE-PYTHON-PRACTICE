#let us consider a movie which has a pg13 rating and try to check the people buying ticket
print("Enter your birthyear here please")
birthyear = int(input())
current_year = 2024
age = current_year - birthyear

if (age<13):
    print("You are not allowed to watch the movie")
else: 
    print("You are allowed to watch the movie")

print("Have a good day")