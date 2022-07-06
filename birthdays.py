birthdays = {'Chung':'May 21', 'Bob':'Dec 12', 'Laura':'May 20'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name ==' ':
        break
    if name in birthdays: 
        print(birthdays[name]+' is birthday of '+ name)
    else:
        print('I do not have birthday information for '+name)
        print('what is their birthday?')
        bday = input()
        birthdays[name] = bday 
        print('Birthday database updated')