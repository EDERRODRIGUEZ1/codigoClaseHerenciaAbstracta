class Color:
    def __init__(self, color):
        self._color = color

    #metodo get
    @property
    def color(self):
        return self._color
    #metodo set
    @color.setter
    def color(self, color):
        self._color = color

    def __str__(self):
        return f'Color[color: {self._color}]'


