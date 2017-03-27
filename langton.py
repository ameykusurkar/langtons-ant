#!/usr/bin/env python3
from collections import defaultdict
from operator import add

class Ant:
    def __init__(self):
        self.grid = defaultdict(bool)
        self.loc = (0, 0)
        self.dir = (1, 0) # Right

    def move(self):
        if self.grid[self.loc]:
            self.turn_left()
        else:
            self.turn_right()

        self.grid[self.loc] = not self.grid[self.loc]
        # Element-wise addition of tuples
        self.loc = tuple(map(add, self.loc, self.dir))

    def turn_right(self):
        (x, y) = self.dir
        self.dir = (y, -x)

    def turn_left(self):
        (x, y) = self.dir
        self.dir = (-y, x)

