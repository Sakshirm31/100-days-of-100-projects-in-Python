print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip you would like to give? 10,12,15 "))
total=bill*(100+tip)/100
print(f"Total bill:${total}")
people=int(input("How many people to split the bill?"))
per_person=total/people
print(f"Your PER PERSON bill is ${round(per_person,2)}")
