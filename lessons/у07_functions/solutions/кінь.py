import random
from _operator import itemgetter


class Solver:
    SIZE = 8

    def __init__(self):
        self.field = [[None] * self.SIZE for _ in range(self.SIZE)]

        self.deltas = list()
        for n0, n1 in [(1, 2), (2, 1)]:
            for m0, m1 in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                self.deltas.append((n0 * m0, n1 * m1))

    def in_range(self, n):
        return 0 <= n < self.SIZE

    def _get_moves(self, row, column):
        for d0, d1 in self.deltas:
            new_row = row + d0
            new_column = column + d1
            if self.in_range(new_row) and self.in_range(new_column) and not self.field[new_row][new_column]:
                yield new_row, new_column

    def make_move(self, row, column, num):
        random.shuffle(self.deltas)
        moves = [
            (r, c, self.count_possible_moves(r, c))
            for r, c in self._get_moves(row, column)
        ]
        if moves:
            new_row, new_column, _ = max(moves, key=itemgetter(2))
            self.field[new_row][new_column] = num
            return new_row, new_column
        return None, None

    def count_possible_moves(self, row, column, depth=2):
        moves = list(self._get_moves(row, column))
        if not depth:
            return len(moves)
        count = 0
        for r, c in moves:
            count += self.count_possible_moves(r, c, depth - 1)
        return count

    def solve(self):
        row, column = 0, 0
        self.field[row][column] = 1
        for i in range(2, self.SIZE ** 2 + 1):
            row, column = self.make_move(row, column, i)
            if row is None:
                break
        for row in self.field:
            row = [f' {n if n else "_":<2}' for n in row]
            print(''.join(row))


Solver().solve()
