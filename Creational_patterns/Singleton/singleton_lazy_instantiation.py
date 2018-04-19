"""
Lazy instantiation makes sure that the object gets created when it’s
actually needed.
"""


class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print(" __init__ method called...")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton() ##  class initialized, but object is not created
Singleton.getInstance() # Object gets created here
s1 = Singleton() ## instance already created

