"""Monostate pattern - all objects sharing the same state."""


class Borg:
    __shared_state = {"1":"2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state


class Borg1(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg1, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


b = Borg()
b1 = Borg()

b.x = 4

## b and b1 are distinct objects
print("Borg Object 'b': ", b)
print("Borg Object 'b1': ", b1)

## b and b1 share same state
print("Object State 'b':", b.__dict__)
print("Object State 'b1':", b1.__dict__)

b2 = Borg1()
b3 = Borg1()
b2.x = 4

## b2 and b3 are distinct objects
print("Borg1 Object 'b2': ", b2)
print("Borg1 Object 'b3': ", b3)

## b2 and b3 share same state
print("Object State 'b2':", b2.__dict__)
print("Object State 'b3':", b3.__dict__)

