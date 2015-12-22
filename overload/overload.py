import inspect

class overload:
    functions = dict()

    def __init__(self, f):
        self.f = f
        f_sig = inspect.signature(f)
        print(f_sig)
        key = '{}_{}'.format(f.__name__, '_'.join([str(a.annotation) for a in
            f_sig.parameters.values()]))
        overload.functions[key] = f

    def __call__(self, *args):
        f_sig = inspect.signature(self.f)
        key = '{}_{}'.format(self.f.__name__, '_'.join([str(a.annotation) for a in
            f_sig.parameters.values()]))
        overload.functions[key](*args)
