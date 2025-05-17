age = int (input()) # int: Read a number as integer from standard input
dob = input() # str: Read a string of format dd/mm/yy from standard input
day, month, year = map(int, dob.split('/')) # int, int, int: Get the correct parts from dob as int

fifth_birthday = f"{day:1d}/{month:1d}/{year+5}" # str: fifth birthday formatted as day/month/year 

last_birthday = f"{day:1d}/{month:1d}/{year+age}" # str: last birthday formatted as day/month/year
new_month = month + 10
new_year = year
if new_month > 12:
    new_month -= 12
    new_year += 1
tenth_month = f"{day:1d}/{new_month:1d}/{new_year}" # str: dob same day after 10 months formatted as day/month/year

# print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space
print(f"{tenth_month}, {fifth_birthday}, {last_birthday}")

weight = float(input()) # float: Read a number as float from stdin(Standard input)
kg = int(weight)
grams = round((weight - kg) * 1000)

weight_readable = f"{kg} kg {grams} grams" # str: reformat weight of format 55 kg 250 grams

# print weight_readable 
print(weight_readable)
