# Nested closures enable another layer of variables to be stored, set during initialization
# A typical use case might be to create slightly different variations of the same function
# based on the value passed during initialization - eg, incrementing by a different amount


def incrementer(increment_value): # Create first level of closure with free variable increment_value

    def inner(start): # Create second level of closure with free variable start
        current = start

        def inc():
            nonlocal current # Set current to a non-local variable so we can directly interact at this level
            current += increment_value # Utilize the increment_value free variable that was created on initialization
            return current # Return functionality
        return inc # Finish inner closure
    return inner # Finish outer closure



# now, incrementer functions can be initialized by nesting functions
increment2 = incrementer(2)
increment2_start100 = increment2(100)

increment10 = incrementer(10)
increment10_start50 = increment10(50)

# initialization MUST occur to create the indirect reference that is stored in memory
