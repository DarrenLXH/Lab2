def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    BMI = weight / (height*height)
    print (str(BMI))
    if BMI<18.5:
        print ("you are under weight")
    else:
        if BMI<25.0:
            print ("you are normal weight")
        else:
            print ("you are over weight")

x = input("Weight=")
y = input("Height=")
calculate_bmi(float(y), float(x))