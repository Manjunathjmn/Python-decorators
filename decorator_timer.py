def time_it(cycles=100): # This is a decorator factory
    '''
    A simple parameterized decorator - timing over a number of cycles.
    Default is 100, can set as many as you want.
    '''
    # Takes in a parameter to pass through to the decorator being
    # In this case, it's the number of cycles to run the function to be timed
    from time import perf_counter # returns current time
    from functools import wraps # preserves metadata
    def inner_decorator(fn):
        @wraps(fn)
        def timer(*args,**kwargs): # take in any arguments
            start = perf_counter() # start timer
            func_result = fn(*args,*kwargs) # feed through and unwrap arguments
            end = perf_counter() # end timer
            for i in range(cycles):
                time_elapsed = end-start #get time elapsed
            args_list = [str(a) for a in args]
            kwargs_list = [f'{k}:{v}' for k,v in kwargs.items()] #extract key value from dict using tuple unpack and list comp.
            average_time = time_elapsed/cycles
            print(f'Function took {time_elapsed} seconds to run.\n'
                  f'Input args: {args_list} and kwargs: {kwargs_list}\n'
                  f'{cycles} cycles were run.\n'
                  f'The average time per cycle was {average_time}.') # Print out how long it took
            return func_result
        return timer
    return inner_decorator