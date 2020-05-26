class myDecorator: # This will be used as a decorator factory.
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __call__(self, fn): # Setup a decorator
        def inner(*args, **kwargs): # Inner function takes the args and kwargs
            # Do something with a and b
            print(f'Parameters were {self.a} and {self.b}.')
            func_result = fn(*args,**kwargs)
            return func_result
        return inner


@myDecorator(10,20) # Use the parameterized decorator.
def simple_add(a,b):
    return a+b


simple_add(1,2) # Basic function call now has added functionality.