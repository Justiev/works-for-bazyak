class Parrot:
    def __init__(self, word):
        self.word = word

    # Изменяет текст для ввода.
    def newText(self, new_word):
        self.word = new_word

    # Произношение текста.
    def say(self):
        print(self.word)

p = Parrot("MyaW")
p.say()
p.newText("ГаВ!")
p.say()