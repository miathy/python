 
def myMBI(weight,height):
    bmi = (weight*703)/(height**2)
    if bmi >= 25:
        print('Overweight')
    elif 18.5 <= bmi < 25:
        print('Normal')
    else:
        print('Underweight') 
    
myMBI(70,60)