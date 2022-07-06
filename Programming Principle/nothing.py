# # for i in range(36,11,-3):
# #     print(i)

# # answer = 'y'

# # while answer =='y':
# #     num1 = int(input('enter  num1: '))
# #     num2 = int(input('enter  num2: '))
# #     sum = num1 + num2
# #     print(sum)
# #     print('do you want to continue?')
# #     answer =  input('enter y to continue: ')

# # print('goodday')
   
# # FEET_TO_INCHES = 12
# # def inchToFeet(inches):
# #     return inches/FEET_TO_INCHES

# # import converter
# # def main():
# #     inches = float(input('Enter inches'))
# #     feet = inchToFeet(inches)
# #     print("Feet: ",format(feet,".3f")

# # days = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
# # for i in days:
# #     print(i.lower())

# f = open("hello.txt", "w")
# f.write("treat each other\n")
# f.write("with respect.")
# f.close()

# f = open("hello.txt", "r")
# var = f.read()
# print(len(var.split(' ')))
# print(var.find('ea')) 


# def main():
#     vote = input('Enter voting rights (Y/N)')
#     medicare = input('Enter medicare rights (Y/N)')
#     if vote=='Y' and medicare =='Y':
#         category = 'citizen'
#     elif vote=='N' and medicare =='N':
#         category = 'TR'
#     else:
#         category = 'PR'
#     print(category)
# main()

# def findOddEven(number):
#     if number %2==0:
#         return 'even'
#     else:
#         return 'odd'

# print(findOddEven(5))

# num =0
# while True:
#     num = int(input('Enter a number: '))    
#     if num <0:
#         break
#     else:
#         print(num, ' is a ', findOddEven(num))
#         print('enter negative num to end')
    
# infile = open("people.txt","w")
# infile.write("Peter\n")
# infile.write("Jeff\n")
# infile.write("Anthony\n")
# infile.write("Nigel\n")
# infile.close()

# try:
#     onfile = open('sales.txt','r')
# except FileNotFoundError:
#     print('cannot open')
# try:
#     if(sale>0):
#         # caculate
# except ZeroDivisionError:
#     print(" number not correct")


# myList1 = ['A', 'C', 'E', 'G', 'I'] 
# # print(myList1[2])
# # print(myList1[3])
# myList1.pop(3)
# myList1.append('K')
# new = list(myList1)
# new.reverse()

# if 'B' in myList1:
#     print('Yes')
# else:
#     print('No')

# print(myList1)
# print(new)

# class InsurancePolicy:
#     def __init__(self,policyNo):
#         self.__No = policyNo
    
#     def get_No(self):
#         return self.__No
    
#     def set_duePayment(self, amount):
#         self.__duePayment = amount
    
#     def get_duePayment(self):
#         return self.__duePayment
# def main():
#     new = InsurancePolicy('P1234')
#     new.set_duePayment(10000)
#     print(new.get_duePayment())


# main()

print(231%2)