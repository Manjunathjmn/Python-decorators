# Closures can be thought of as a function plus an extended scope that contains the free variables
# This free variable is shared between scopes via an intermediary cell with points to
# an object that contains the value (an indirect reference)


def outer():
    a = 100  # local (outer) scope
    x = 'python'

    def inner():
        a = 10  # local (inner) scope
        print(x)  # reference to variable x bound to outer scope
    return inner  # create closure


fn = outer()  # inner is returned, call with fn()


# Introspection can be done through dunder methods
fn.__code__.co_freevars  # returns tuple of all free variables
fn.__closure__  # returns tuple of cell to object addresses

