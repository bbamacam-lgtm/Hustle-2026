
# Breena Bamaca|Lab 5|Intro to Python

# Ticket 1
ages = [17, 11, 25, 13, 9]

for age in ages:
    print(age)
    if age < 13:
        print("Too young")
    else:
        print("Access granted")
# PREDICT: 17, 25, 13 get "Access granted" and 11, 9 get "Too young"
# the variable age holds a value each time it loops.

# Ticket 2
keep_checking = "yes"
while keep_checking == "yes":
    age = int(input("How old are you? "))
    if age < 13:
        print("Too young")
    else:
        print("Access granted")
    keep_checking = input("Do you want to check again? (yes/no) ")
# PREDICT: if user inputs no then loop doesn't run
# while loop will keep running until user inputs no, then it will stop.

# Ticket 3
while True:
   entry = input("Enter an age or type stop: ") 
   if entry == "stop":
         break          # exits loop
# PREDICT: the loop won't ever end
# this while loop will keep running until user inputs "stop", then it will break the loop and exit.

# Ticket 4
def can_access(age):
    if age < 13:  
        return False
    else:
        return True
# PREDICT: the code in Ticket 1 does't use boolean values
# it is efficent

# Ticket 5
signup_report = [22, 10, 15, 8, 19, 13]
for num, item in enumerate(signup_report, start=1):
    print(f"Signup #{num} | Age {item}")
    if can_access(item):
        print("Access granted")
    else:
        print("Too young")
# PREDICT: signup #1 22 acess granted, signup #2 10 too young, signup #3 15 access granted, signup #4 8 too young, signup #5 19 access granted, signup #6 13 access granted
# for loops, enumerate() function, and f-strings 
