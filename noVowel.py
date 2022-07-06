def noVowel(x):
    #vowel = ['u', 'e','o','a','i','U','E','O','A','I']

    if x in ('ueoaiUEOAI'):
        return False
    else:
        return True


noVowel('a')