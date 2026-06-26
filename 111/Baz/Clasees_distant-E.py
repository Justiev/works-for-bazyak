from random import choice


class Parrot:
    def __init__(self, word):
        self.words = []     # Список фраз, которые объект может произнести.
        self.words.append(word)

    # Учит новую фразу и добавляет в список фраз.
    def learn(self, new_word):
        self.words.append(new_word)
    
    
    def say(self, n=1):
        if n > 1:
            for _ in range(n):
                word = choice(self.words)   # Фраза выбирается случайно из списка.
                print(word, end=' ')
            print('\n')
        else:
            print(choice(self.words))


p = Parrot("MyaW")
p.say()
p.learn("ГаВ!")
p.say(3)
p.say()