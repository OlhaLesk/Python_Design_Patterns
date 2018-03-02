class Singleton(object):

    """Overrides the __new__ method (Python’s special method to
    instantiate objects) to control the object creation.
    """

    def __new__(cls):
        """Creates a new object but at first checks whether the object
        already exists (the hasattr method checks if an object has the
        instance property).
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()
print("Object created", s)
s1 = Singleton()
print("Object created", s1)

