#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Copyright 2013-2014 European Commission (JRC);
# Licensed under the EUPL (the 'Licence');
# You may not use this work except in compliance with the Licence.
# You may obtain a copy of the Licence at: http://ec.europa.eu/idabc/eupl

from __future__ import division, unicode_literals

import unittest
from unittest.case import skipIf

from wltp import utils
from wltp.tkui import TkWltp


try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk


class TkUiTest(unittest.TestCase):


    @skipIf(utils.is_travis(), "TravisCI has no XServer!")
    def test_smoke_test_no_event_loop(self):
        root = tk.Tk()
        try:
            app = TkWltp(root)
            app.master.quit()
        finally:
            root.destroy()

    @skipIf(utils.is_travis(), "TravisCI has no XServer!")
    def test_smoke_test_with_event_loop(self):
        root = tk.Tk()
        try:
            app = TkWltp(root)
            app.master.after_idle(app.do_about)
            app.master.after_idle(app.do_reset)
            app.master.after_idle(app.master.quit)
            app.mainloop()
        finally:
            root.destroy()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
