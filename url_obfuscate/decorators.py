# -*- encoding: utf-8 -*-
from functools import wraps
import helpers

def deobfuscate(view_func):
    def wrapper(request, *args, **kwargs):
        new_kwargs = dict()
        for key, value in kwargs.iteritems():
            if value:
                new_kwargs[key] = helpers.deobfuscate(str(value))
            else:
                new_kwargs[key] = value
        return view_func(request, *args, **new_kwargs)
    return wraps(view_func)(wrapper)
