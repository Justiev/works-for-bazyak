class LampRow:
    
    # Данные хрянятся в виде целого числа.
    def __init__(self, quantity):
        self.quantity = quantity
        self._state_int = 0

    # Преобразует в обычный вид.
    @property
    def state(self):
        return format(self._state_int, f'0{self.quantity}d')

    # Записывает и преобразует в обычный вид.
    @state.setter
    def state(self, new_state):
        if len(new_state) == self.quantity:
            self._state_int = int(new_state)
        else:
            self._state_int = 0

    
    def show(self):
        current_state_str = self.state 
        display = ""
        for i in current_state_str:
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