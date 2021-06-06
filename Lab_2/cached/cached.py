import inspect


def cached(func):
    keys = list()
    results = list()
    data = inspect.getfullargspec(func)
    names = data[0]

    def wrapped(*args, **kwargs):
        _kwargs = kwargs.copy()
        args_count = len(args)

        _args = dict()

        for i in range(min(len(names), args_count)):
            _args[names[i]] = args[i]

        while args_count < len(names):
            _args[names[args_count]] = kwargs[names[args_count]]
            del _kwargs[names[args_count]]
            args_count += 1

        if data[1] is not None:
            _args['args'] = args[len(names):]

        if data[2] is not None:
            _args['kwargs'] = _kwargs

        if _args in keys:
            print("Got it")
            return results[keys.index(_args)]
        else:
            print("Nope")
            keys.append(_args)
            results.append(func(*args, *kwargs))
            return results[keys.index(_args)]
    return wrapped


@cached
def func(a, b):
    return a + b


print(func(11, 15))
print(func(11, b=15))
print(func(b=15, a=11))