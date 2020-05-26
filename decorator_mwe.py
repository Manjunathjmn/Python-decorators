def decorator_mwe(fn): # Decorators take in the function
    '''
    A simple minimum working example of a decorator - no functionality.
    '''
    # A free variable can be defined here for storage and use.
    def inner(*args,**kwargs):
        # Typically something is done here - e.g. timing, memoization etc.
        func_result = fn(*args,**kwargs)
        return func_result # Closure returns the function result
    return inner # Decorators return the function result, with some additional functionality