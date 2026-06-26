class Parrot:
    # Фраза записывается в свойствах класса.
    def __init__(self, word):
        self.word = word
    
    # Произносит фразу, которую введут при объявлении класса.
    def say(self):
        print(self.word)


p1 = Parrot("MyaW")
p2 = Parrot("Гав!")

p1.say()
p2.say()