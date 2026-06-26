class Parrot:
    def __init__(self, word):
        self.word = word


    # Изменяет текст для ввода.
    def newText(self, new_word):
        self.word = new_word

    
    # Произношение с повторением.
    def say(self, n=1):
        if n > 1:
            for _ in range(n):
                print(self.word, end=' ')
            print('\n')
        else:
            print(self.word)


p = Parrot("MyaW")
p.say()
p.newText("ГаВ!")
p.say(3)