#asking for input from the users
height=float(input("Enter the height in cm:"))
weight=float(input("Enter the weight in kg:"))

#define a function for BMI 
BMI=weight/(height/100)**2

#printing the BMI
print("your body mass index is",BMI)

#using the if-elif-else conditions
if BMI<=18.5:
    print("ohhh!you are underweight.")
elif BMI<=24.9:
    print("AWESOME!you are healthy.")
elif BMI<=29.9:
    print("OOPS!you are overweight.")
else:
    print("AMMM!your are obese..")



    