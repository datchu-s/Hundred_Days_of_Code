# This programme calculates the tip and splits the bill
print("Welcome to tips calculator")
bill = float(input('What is the bill amount?: '))
tip = int(input('What percantage of tip you would like to give? 10, 12 or 15?: '))
visitors = int(input('How many people are there to split the bill?: '))

splitted_bill = round((bill + bill * (tip/100) )/visitors, 2)
print(f"Each person should pay: {splitted_bill}")