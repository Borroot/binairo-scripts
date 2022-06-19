# TODO add conversion from codex to grid and load all

def texttogrid(text, size):
    """ Convert a string to an actual grid puzzle. """
    grid = [[None] * size for _ in range(size)]
    count = 0
    for c in text:
        if   c == "0":
            grid[count // size][count % size] = 0
            count += 1
        elif c == "1":
            grid[count // size][count % size] = 1
            count += 1
        else:
            count += ord(c) - ord('a') + 1
    return grid


def loadpuzzles(filename):
    """ Load all the lines in the file and return them as puzzle solution pairs.
    Expects every line to be as <size puzzle solution>. """
    with open(filename) as fp:
        lines = [line.strip() for line in fp.readlines()]
        lines = filter(lambda s: not str.isspace(s) and s != "", lines)
        lines = map(lambda s: {
            "puzzle": texttogrid(s.split(' ')[1], int(s.split(' ')[0])),
            "solution": texttogrid(s.split(' ')[2], int(s.split(' ')[0]))}, lines)
        return list(lines)
