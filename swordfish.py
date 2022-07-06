while True:
    print('Who are you? Enter your name: ')
    name = input()
    if name == 'Mai':
        print(' Hello Mai. What is your password?')
        while True:
            password = input()
            if password != 'swordfish':
                print('Enter again:')
            else:
                print('Access granted')
                break
        break
    

        
