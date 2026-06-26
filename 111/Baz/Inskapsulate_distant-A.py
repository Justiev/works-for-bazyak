class LampRow:

    def __init__(self):
        self._state = "00000000"
    
    # Функция возвращает значение.
    @property
    def state(self):
        return self._state
    
    # Функция вводит новое значение.
    @state.setter
    def state(self, new_state):
        if len(new_state) == 8:
            self._state = new_state
        else:
            self._state = "00000000"

    # Выводит горящие лампочки.
    def show(self):

        display = ""

        for i in self._state:
            if i == '1':
                display += "*"
            else:
                display += "-"
                
        print(display)


lamps = LampRow()
lamps.show()
lamps.state = "10101010"
print(lamps.state)
lamps.show()