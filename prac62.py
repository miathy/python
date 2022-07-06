def rlookup(phonebook):

    while True:
        number = input('Enter phone number in the format (xxx)xxx-xx-xx: (or blank space to exit')
        if number in phonebook:
            print(phonebook[number])
        else:
            print('The number you enter is not in use.')
        


rphonebook = {
    '(123)456-78-910':['anna','karenina'],
    '(901)234-56-78':['yu','tsun'],
    '(321)908-76-54':['hans','castorp'],
}

rlookup(rphonebook)