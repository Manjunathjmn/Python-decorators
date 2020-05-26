# A similar functionality can be achieved using a class with a single method
# In general, these types of classes can be replaced by closured


def averager():
    '''
    Takes in integers and returns a running total
    '''
    count = 0
    total = 0

    def inner(num):
        nonlocal count
        nonlocal total
        total += num
        count += 1
        return 0 if count == 0 else total/count
    return inner


# Again, as this is a closure we need to initialize a function that uses it

running_average = averager()

