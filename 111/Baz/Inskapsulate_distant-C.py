class LampRow:
    def __init__(self, quanity):
        self.quanity = quanity
        self._state = "0" * self.quanity
    

    @property
    def state(self):
        return self._state

    # Функция вводит новое значение и может изменить количество ламп.
    @state.setter
    def state(self, new_state):
        if len(new_state) == self.quanity:
            self._state = new_state
        else:
            self._state = "0" * self.quanity

    # Здесь существуют 2 типа цвета: 1 - красный, 2 - зелёный.
    def show(self):
        display = ""
        for i in self._state:
            if i == '1':
                display += "*"
            elif i == '2':
                display += "o"
            else:
                display += "-"
                
        print(display)

lamps = LampRow(6)
lamps.show()
lamps.state = "102102"
print(lamps.state)
lamps.show()
lamps.state = "10201010"
print(lamps.state)
lamps.show()