# Closures enables the free-variable to be stored for each instance of the function
# This occurs through the cell-indirect reference system
# A new cell-indirect reference is created in memory for each instance of the function

# A simple counter can be created with a closure, with the non-local variable stored
# and modified within the inner function


def counter(*args):
    '''
    :param args:
    Initialized with no argument
    Pass integers to the initialized function to increment the stored count by n
    :return:
    Returns stored count
    '''
    count = 0  # local (outer) scope

    def inner(num: int):
        nonlocal count  # set count to non-local variable so we can modify it in this scope
        print(f'Previous count was {count}.\n'
              f'Incrementing count by {num}.')
        count += num
        print(f'New count is {count}')
    return inner  # create closure

# Introspection can be done through dunder methods
    # fn.__code__.co_freevars  # returns tuple of all free variables
    # fn.__closure__  # returns tuple of cell to object addresses


counter1 = counter()


counter2 = counter()
