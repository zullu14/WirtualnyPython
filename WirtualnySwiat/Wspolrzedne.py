
class Wspolrzedne(object):

    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0

    def __eq__(self, other):
        if isinstance(other, Wspolrzedne):
            return self.x == other.x and self.y == other.y
        return False

    def __ne__(self, other):
        if isinstance(other, Wspolrzedne):
            return self.x != other.x or self.y != other.y
        return False
