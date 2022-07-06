a, b = int(input("Enter first number: ")), int(input("Enter second number: "))
 
if a > b:
    trend = "decreasing"
elif a < b:
    trend = "increasing"
else:
    trend = "unchanging"
 
# save last number
last = b
 
# keep asking for another number
while (num := int(input("Enter next number: "))) != -1:
    # if trend is inconsistent, skip
    if trend != "inconsistent":
        # conditions to determine inconsistent trend
        if (trend == "decreasing" and num >= last) or (trend == "increasing" and num <= last) or (trend == "unchanging" and num != last):
            trend = "inconsistent"
 
    # update last number
    last = num
 
result = "The sequence has a " + trend + " trend."
print(result)
   


    