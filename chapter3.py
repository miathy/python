#3.24
#lst = input('enter a list:').split(',')
#for i in lst:
 #   if i != 'secret':
  #      print(i)

#3.25
#names = input('enter names:').split(',')
#for name in names:
 #   if name.strip()[0].lower() in 'abcdefghijkl':
  #      print(name)

#3.26
#lst = input('Enter a list of numbers:')
#if len(lst)==0:
 #   print('Please enter a list:')
#else:
 #   print('the first element is: ' + lst[0])
  #  print('the last element is: '+lst[-1])

#3.27
#n = int(input('enter n: '))
#for i in range(4):
#  print(n*i)

#3.28
#n = int(input('enter n: '))
#for numb in range(n):
#  print(numb**2)

#3.29
#n = int(input('enter n:'))
#for numb in range(1,n+1):
 # if n%numb == 0:
  #  print(numb)

#3.30

n1 = int(input('enter 1st number: '))
n2 = int(input('enter 2nd number: '))
n3 = int(input('enter 3rd number: '))
n4 = int(input('enter the last number: '))

avg1 = (n1+n2+n3)/3
if avg1 == n4:
  print('Equal')



