# def main():
#     value = 5
#     show_double(value)

# def show_double(number):
#     result = number * 2
#     print('result: ', result)

# main()
# def main():
#     texas()
#     california()

# def texas():
#     birds = 5000
#     print('texas has ', birds, 'birds.')

# def california():
#     birds = 8000
#     print('california has ', birds, 'birds.')

# main()
# def main():
#     print('finding the sum of two value:')
#     val1 = int(input('enter value 1: '))
#     val2 = int(input('enter value 2: '))
#     show_sum(val1, val2)
# def show_sum(num1, num2):
#     total = num1 + num2
#     print('total: ', total)

# main()
# def main():
#     value = 99
#     print('the value is', value)
#     change_me(value)
#     print('back in main, the value is ', value)
# def change_me(arg):
#     print('im changing the value')
#     arg =0
#     print(' now the value is', arg)
# main()
# def main():
#     show_interest(rate = 0.01, period = 10, principal = 10000)

# def show_interest (principal, rate, period):
#     interest = principal * rate * period
#     print('The simple interest will be $', \
#         format(interest, ',.2f'), sep=' ')

# main()

# def main():
#     first_name = input('enter first name:')
#     last_name = input('enter last name:')
#     reverse_name(last = last_name, first = first_name)
# def reverse_name(first, last):
#     print(last, first)

# main()

# my_value = 10

# def main():
#     print(' the value is', my_value)
#     show_value()
#     show_double()

# def show_value():
#     global my_value
#     my_value = 30
#     print('the value is ', my_value)

# def show_double():
#     print(' doubled value is', my_value *2)
#     print(my_value)
# main()
# import random
# def main():
#     for count in range(5):
#         print(random.randint(1,100))
# main()   


# import math
# def main():
#     res = 'y'
#     while res =="y" or res =="Y":
#         number = float(input("enter number: "))
#         square_root = math.sqrt(number)
#         print('square root of ', number, 'is', square_root)
#         res = input('\ndo you want to repeat? (y/n): ')

# main()
discount_percent = 0.2
def main():
    reg_price = get_regular_price()
    sale_price = reg_price - discount(reg_price)
    print('the sale price is $', format(sale_price, ',.2f'), sep =' ')

def get_regular_price():
    price = float(input("enter the item's regular price: "))
    return price

def discount(price):
    return price * discount_percent

main()