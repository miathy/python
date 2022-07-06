# get user input
 
a, b = int(input("Enter the first number in the sequence: ")), int(input("Enter second number: "))

# detect the trend
if a > b:
    trend = "decreasing"
else:
    trend = "increasing"

# save last number
last = b 
print('Enter the subsequence numbers, -1 to finish')

# keep asking for another number
while (num := int(input('Enter next number: '))) != -1:
    #check the trend of subsequence numbers
    if trend == "decreasing" and last > num:
        trend = "decreasing"
    elif trend == 'increasing' and last < num:
        trend = "increasing"
    else:
        trend = 'inconsistent'

    # update last number
    last = num

#print output
if trend == 'inconsistent':
    print('\nThere is no consistent trend in the sequence.')
else:
    print('\nThe sequence has a ' + trend + ' trend.')

    