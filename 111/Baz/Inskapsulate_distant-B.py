class LampRow:

    # Количество ламп задаётся в начале.
    def __init__(self, quanity):
        self.quanity = quanity
        self._state = "0" * self.quanity

    # Функция возвращает значение.    
    @property
    def state(self):
        return self._state

    # Функция вводит новое значение.
    @state.setter
    def state(self, new_state):
        if len(new_state) == self.quanity:
            self._state = new_state
        else:
            self._state = "0" * self.quanity

    def show(self):
        display = ""
        for i in self._state:
            if i == '1':
                display += "*"
            else:
                display += "-"
                
        print(display)

lamps = LampRow(6)
lamps.show()
lamps.state = "101010"
print(lamps.state)
lamps.show()
lamps.state = "10101010"
print(lamps.state)
lamps.show()