import operator

class Position(object):
    __slots__ = (
        'facing', 'x', 'y', 'MAPPING', 'OPERATORS', 'position', 'distance'
    )

    MAPPING = {
        'N': {'L': 'W', 'R': 'E'},
        'S': {'L': 'E', 'R': 'W'},
        'W': {'L': 'S', 'R': 'N'},
        'E': {'L': 'N', 'R': 'S'},
    }
    OPERATORS = {
        'N': ('y', operator.add),
        'S': ('y', operator.sub),
        'E': ('x', operator.add),
        'W': ('x', operator.sub)
    }

    def __init__(self, facing, x, y):
        self.facing  = facing
        self.x       = x
        self.y       = y

    @property
    def position(self):
        """
        Return the cartesian co-ordinates.
        """
        return self.x, self.y

    @property
    def distance(self):
        """
        Return the absolute distance from the starting point.
        """
        return abs(self.x) + abs(self.y)

    def turn(self, direction):
        """
        Set the new direction.
        """
        self.facing = self.MAPPING[self.facing][direction]

    def move(self, blocks):
        """
        Jump to the end of the move.
        """
        if   self.facing == 'N': self.y += blocks
        elif self.facing == 'S': self.y -= blocks
        elif self.facing == 'E': self.x += blocks
        elif self.facing == 'W': self.x -= blocks

    def move_slowly(self, blocks):
        """
        Move one block at a time, and mark all visited co-ordinates.
        """
        visits = []
        attrib, op = self.OPERATORS[self.facing]
        for _ in xrange(blocks):
            setattr(self, attrib, op(getattr(self, attrib), 1))
            visits.append(self.position)
        return visits
        
    def __str__(self):
        return '<Direction="{}" (x,y)=({},{}) distance={}>'.format(
            self.facing, self.x, self.y, self.distance
        )


def run_steps_1(directions):
    p = Position('N', 0, 0)
    for step in directions:
        direction, blocks = step[0], int(step[1:])
        p.turn(direction)
        p.move(blocks)
    print p


def run_steps_2(directions):
    p = Position('N', 0, 0)
    duplicates = set()
    already_seen = False
    for step in directions:
        direction, blocks = step[0], int(step[1:])
        p.turn(direction)
        visits = p.move_slowly(int(blocks))
        for v in visits:
            if v in duplicates:
                print 'Duplicate location :: {}'.format(v)
                already_seen = True
                break
            else:
                duplicates.add(v)
        if already_seen:
            break


if __name__ == '__main__':
    directions = "R1, L3, R5, R5, R5, L4, R5, R1, R2, L1, L1, R5, R1, L3, L5, L2, R4, L1, R4, R5, L3, R5, L1, R3, L5, R1, L2, R1, L5, L1, R1, R4, R1, L1, L3, R3, R5, L3, R4, L4, R5, L5, L1, L2, R4, R3, R3, L185, R3, R4, L5, L4, R48, R1, R2, L1, R1, L4, L4, R77, R5, L2, R192, R2, R5, L4, L5, L3, R2, L4, R1, L5, R5, R4, R1, R2, L3, R4, R4, L2, L4, L3, R5, R4, L2, L1, L3, R1, R5, R5, R2, L5, L2, L3, L4, R2, R1, L4, L1, R1, R5, R3, R3, R4, L1, L4, R1, L2, R3, L3, L2, L1, L2, L2, L1, L2, R3, R1, L4, R1, L1, L4, R1, L2, L5, R3, L5, L2, L2, L3, R1, L4, R1, R1, R2, L1, L4, L4, R2, R2, R2, R2, R5, R1, L1, L4, L5, R2, R4, L3, L5, R2, R3, L4, L1, R2, R3, R5, L2, L3, R3, R1, R3".replace(',', '').split()

    run_steps_1(directions)
    run_steps_2(directions)

