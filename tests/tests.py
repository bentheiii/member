from math import sqrt
from unittest import TestCase

from member import member


class MemberTest(TestCase):
    class A:
        def __init__(self, x):
            self.x = x
            self.bar_runs = 0

        @member
        def foo(self):
            return self.bar(1)

        @member
        def bar(self, y):
            self.bar_runs += 1
            return sqrt(self.x * y)

    def test_run_once(self):
        a = self.A(16)
        self.assertEqual(a.foo(), 4)
        self.assertEqual(a.foo(), 4)
        self.assertEqual(a.bar_runs, 1)
        del a.foo
        self.assertEqual(a.foo(), 4)
        self.assertEqual(a.bar_runs, 1)
        self.assertEqual(a.bar(9), 12)
        self.assertEqual(a.bar(9), 12)
        self.assertEqual(a.bar_runs, 2)
        a.bar.pop(9)
        self.assertEqual(a.bar(9), 12)
        self.assertEqual(a.bar_runs, 3)


class SlotsTest(TestCase):
    class A:
        __slots__ = 'x', 'bar_runs', '_foo', '_bar'

        def __init__(self, x):
            self.x = x
            self.bar_runs = 0

        @member
        def foo(self):
            return self.bar(1)

        @member
        def bar(self, y):
            self.bar_runs += 1
            return sqrt(self.x * y)

    def test_run_once(self):
        a = self.A(16)
        self.assertEqual(a.foo(), 4)
        self.assertEqual(a.foo(), 4)
        self.assertEqual(a.bar_runs, 1)
        del a.foo
        self.assertEqual(a.foo(), 4)
        self.assertEqual(a.bar_runs, 1)
        self.assertEqual(a.bar(9), 12)
        self.assertEqual(a.bar(9), 12)
        self.assertEqual(a.bar_runs, 2)
        a.bar.pop(9)
        self.assertEqual(a.bar(9), 12)
        self.assertEqual(a.bar_runs, 3)

# todo test slots
