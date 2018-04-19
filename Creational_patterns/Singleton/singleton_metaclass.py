import  sqlite3
#class MyInt(type):
#    def __call__(cls, *args, **kwargs):
#        print("Here's My int:", args)
#        return type.__call__(cls, *args, **kwargs)
#
#
#class int(metaclass=MyInt):
#
#    """Sample metaclass."""
#
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
#
#
#i = int(4,5)


class MetaSingleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Create a Singleton."""
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args,
                                                                     **kwargs)
        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):

    pass


class Database(metaclass=MetaSingleton):

    """Manage database connection.

    When the web app wants to perform certain operations on the DB, it
    instantiates the database class multiple times, but only one object
    gets created. Thus, calls to the database are synchronized. This is
    inexpensive on system resources.
    If instead of having one webapp, we have a clustered setup with
    multiple web apps but only one DB, this is not a good situation for
    Singletons. With every web app addition, a new Singleton gets created
    and a new object gets added that queries the database. This results
    in unsynchronized database operations and is heavy on resources. In
    such cases, database connection pooling is better.
    """

    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


logger1 = Logger()
logger2 = Logger()
print("Logger Object logger1", logger1)
print("Logger Object logger2", logger2)

db1 = Database().connect()
db2 = Database().connect()
print("Database Object DB1", db1)
print("Database Object DB2", db2)

