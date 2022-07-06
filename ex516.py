def indexes(word,letter):
    lst = []
    for i,c in enumerate(word):
        if c == letter: 
            lst.append(i)
    print(lst) 

#def indexes(word, letter):
 #   lst =[]
  #  for char in word:
   #     if char == letter:
    #        a = word.index(char) # word.index(char) only return the first index of char
     #       lst.append(a) 
    #print(lst) 

indexes('mississippi','s')           