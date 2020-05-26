# This is a minimum working example of a class decorator.
# Here we monkey-patch a new method onto an existing class, called 'added_method'.


def class_decorator(cls): # Pass in an entire class to be decorated
    #Add functionality with a closure (decorator)
    def inner(self): # Define some functionality that the new method will achieve
        # Self passes through all the instance attributes
        # Do something with the self --
        # For example, print something
        print(f'My numerator is {self.denominator}')
        # Or return some transformation of the self.attributes
    cls.added_method = inner # Define the name of the new method
    return cls #Return the entire class back out with added functionality

Fraction = class_decorator(Fraction)
f1 = Fraction(1,2)
f1.added_method()