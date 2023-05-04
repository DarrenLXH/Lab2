def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    BMI = weight / (height*height)
    print (str(BMI))
    if BMI<18.5:
        print ("you are under weight")
        return -1
    else:
        if BMI<25.0:
            print ("you are normal weight")
            return 0
        else:
            print ("you are over weight")
            return 1
calculate_bmi(weight=57, height=1.73)

