#! python
#-*- coding: utf-8 -*-
#
# Copyright 2013-2014 European Commission (JRC);
# Licensed under the EUPL (the 'Licence');
# You may not use this work except in compliance with the Licence.
# You may obtain a copy of the Licence at: http://ec.europa.eu/idabc/eupl

from __future__ import division, unicode_literals

import argparse
import os
import unittest

import pandas as pd


##############
#  Compatibility
#
try:
    assertRaisesRegex = unittest.TestCase.assertRaisesRegex
except:
    assertRaisesRegex = unittest.TestCase.assertRaisesRegexp

## Python-2 compatibility
#
try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError  # @ReservedAssignment
else:
    FileNotFoundError = OSError  # @ReservedAssignment

def raise_ex_from(ex_class, chained_ex, *args, **kwds):
 from six import reraise


##############
#  Utilities
#
def str2bool(v):
    vv = v.lower()
    if (vv in ("yes", "true", "on")):
        return True
    if (vv in ("no", "false", "off")):
        return False
    try:
        return float(v)
    except:
        raise argparse.ArgumentTypeError('Invalid boolean(%s)!' % v)


def pairwise(t):
    '''From http://stackoverflow.com/questions/4628290/pairs-from-single-list'''
    it1 = iter(t)
    it2 = iter(t)
    try:
        next(it2)
    except:
        return []
    return zip(it1, it2)


def ensure_modelpath_Series(mdl, json_path):
    import jsonpointer as jsonp

    part = jsonp.resolve_pointer(mdl, json_path)
    if not isinstance(part, pd.Series):
        part = pd.Series(part)
        jsonp.set_pointer(mdl, json_path, part)

def ensure_modelpath_DataFrame(mdl, json_path):
    import jsonpointer as jsonp

    part = jsonp.resolve_pointer(mdl, json_path)
    if not isinstance(part, pd.Series):
        part = pd.DataFrame(part)
        jsonp.set_pointer(mdl, json_path, part)


## From http://code.activestate.com/recipes/578231-probably-the-fastest-memoization-decorator-in-the-/
#
def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)




## From http://stackoverflow.com/a/4149190/548792
#
class Lazy(object):
    def __init__(self,func):
        self.func=func
    def __str__(self):
        return self.func()


def is_travis():
    return 'TRAVIS' in os.environ

def generate_filenames(filename):
    f, e = os.path.splitext(filename)
    yield filename
    i = 1
    while True:
        yield '%s%i%s' % (f, i, e)
        i += 1
    