class Object:
    '''
    Objects could be numbers or operations (+,-,...)

    attributes:
    x-coordinate position on screen, y-coordinate, distance from the cursor
    '''
    x: float
    y: float
    distance: float

    def __init__(self, x: float, y: float, distance: float):
        self.x, self.y, self.distance = x, y, distance

    def grab(self, cur_x, cur_y, set_dist):
        '''
        this method is used to grab the object
        '''

        distance2Cursor = ((cur_x - self.x) ** 2 + (cur_y - self.y) ** 2) ** 0.5

        return distance2Cursor < set_dist


class Number(Object):
    '''
    this is a number object with coordinates, distance and some int value
    '''
    x: float
    y: float
    distance: float
    value: int

    def __init__(self, x: float, y: float, distance: float, value: int):
        Object.__init__(self, x, y, distance)
        self.value = value


class Operations(Object):
    '''
    this is an operation with value '*' or '-' or '+' or '/'
    and the normal object attributes x,y coordinates and distance from cursor
    '''
    x: float
    y: float
    distance: float
    value: str

    def __init__(self, x: float, y: float, distance: float, value: str):
        Object.__init__(self, x, y, distance)
        self.value = value

class Answer(Object):
    '''
    this is an answer object with coordinates, distance and some int value
    '''
    x: float
    y: float
    distance: float
    value: int

    def __init__(self, x: float, y: float, distance: float, value: int):
        Object.__init__(self, x, y, distance)
        self.value = value


class GarbageCan(Object):
    '''
    this is a garbage Object with constant coordinates on the bottom left
    and a distance that is passed in as a parameter by the user
    '''
    x: int
    y: int
    distance: float

    def __init__(self, distance: float):
        self.x = 20
        self.y = 350
        self.distance = distance
        self.value = "Garbage.png"

class Squares(Object):
    '''
    this is a squares Object with two coordinates, both passed in by the user, 
    and a distance that is passed in as a parameter by the user
    '''

    x: float
    y: float
    distance: float

    def __init__(self, x: float, y: float, distance: float):
        Object.__init__(self, x, y, distance)
        self.value = "Green Square.png"

class Circle(Object):
    '''
    This is a circles Object wiht two coordinates, both passed in by the user, and a distance
    that is passed in as a parameter by a user.
    '''

    x: float
    y: float
    distance: float

    def __init__(self, x: float, y: float, distance: float):
        Object.__init__(self, x, y, distance)
        self.value = "Circle.png"


class Equals(Object):
    '''
    This is a equals_sign Object wiht two coordinates, both passed in by the user, and a distance
    that is passed in as a parameter by a user.
    '''

    x: float
    y: float
    distance: float

    def __init__(self, x: float, y: float, distance: float):
        Object.__init__(self, x, y, distance)
        self.value = "Equals Sign.jpg"