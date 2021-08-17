# __init__ function using inheritance
'''Inheritance is the procedure in which one class inherits the attributes and methods of another class.
 The class whose properties and methods are inherited is known as Parent class.
 And the class that inherits the properties from the parent class is the Child class.'''
class A(object):
    def __init__(self, something):
        print("A init called")
        self.something = something


class B(A):
    def __init__(self, something):
        # Calling init of parent class
        A.__init__(self, something)
        print("B init called")
        self.something = something

obj = B("Something")