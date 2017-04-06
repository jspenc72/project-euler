import functools

def memoize(f):
    _f={}
    @functools.wraps(f)
    def mem_f(*args):
        if args in _f:
            return _f[args]
        else:
            ret = f(*args)
            _f[args] = ret
            return ret
    return mem_f
