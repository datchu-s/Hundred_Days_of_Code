#Assuming the life expentancy of a person as 90, printing the remaining available time in terms of week.
age = int(input('Enter your age: '))
remaining_years_in_weeks = (90 - age)*52
print(f"You have {remaining_years_in_weeks} left")