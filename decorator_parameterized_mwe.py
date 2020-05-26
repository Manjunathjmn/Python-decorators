def paramdec_mwe(a,b): # A decorator factory
    '''
    A minimum working example for a parameterized decorator.
    '''
    from functools import wraps
    def internal_decorator(fn): # Start of the internal decorator
        @wraps(fn)
        def inner(*args,**kwargs):
            print(f'The parameters for the decorator were {a} and {b}.')
            # The parameters a and b are passed down through all the levels as a free variable.
            function_result = fn(*args,**kwargs)
            return function_result
        return inner # End of the internal decorator.
    return internal_decorator # The decorator factory returns a decorator.