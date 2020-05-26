# Nested closures enable another layer of variables to be stored, set during initialization
# A typical use case might be to create slightly different variations of the same function
# based on the value passed during initialization - eg, incrementing by a different amount


def incrementer(increment_value):

    def inner(start):
        current = start

        def inc():
            nonlocal current
            current += increment_value
            return current
        return inc
    return inner


# now, incrementer functions can be initialized by nesting functions
increment2 = incrementer(2)
increment2_start100 = increment2(100)

increment10 = incrementer(10)
increment10_start50 = increment10(50)

# initialization MUST occur to create the indirect reference that is stored in memory
