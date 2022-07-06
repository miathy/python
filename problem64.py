def wordcount(text):
    wordlst = text.split()
    counters = {}

    for word in wordlst:
        if word in counters:
            counters[word]+=1
        else:
            counters[word] = 1
    for word in counters:
        if counters[word]==1:
            print('{:8} appear {} time.'.format(word,counters[word]))
        return counters

t= 'all animals are equal but some animals are more equal than others'

wordcount(t)