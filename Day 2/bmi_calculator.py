print("Lets calculate BMI")
height = float(input("Enter your height in metres: "))
weight = int(input("Enter your weight in kilograms: "))

bmi = round(weight/height**2,2)
print('Your Body Mass Index (BMI) is:{}'.format(bmi))
print("Code updated")