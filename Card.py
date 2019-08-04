class Card():
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        return "{} - {}".format(self.color, self.number)