def four_letter(lst):
    sublst = []
    for word in lst:
        if len(word) == 4:
            sublst.append(word)
    print(sublst)

four_letter(['dog','letter','stop','door'])
