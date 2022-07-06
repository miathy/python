class Animal:
    def __init__(self, species = 'animal', language = 'make sounds'):
        self.spec = species
        self.lang = language
    def speak(self):
        print(' I am a {} and I {}.'.format(self.spec,self.lang))

snoopy = Animal('dog','bark')
snoopy.speak()

    

      