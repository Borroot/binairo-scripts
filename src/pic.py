from PIL import Image, ImageDraw, ImageFont


_MAGNIFIER = 350
_LINEWIDTH = _MAGNIFIER // 20


def _draw_box(x, y):
    """ Return the top left coordinates and the bottom right coordinates of the
    requested cell. """
    top = (x * _MAGNIFIER + _LINEWIDTH, y * _MAGNIFIER + _LINEWIDTH)
    bot = ((x + 1) * _MAGNIFIER, (y + 1) * _MAGNIFIER)
    return top, bot


def _draw_background(draw):
    """ Draw a black square for the background. """
    draw.rectangle((0, 0) + draw.im.size, fill='black')


def _draw_text(draw, x, y, text):
    """ Draw the given text (number) in the given cell. """
    top, bot = _draw_box(x, y)
    middle = ((top[0] + bot[0]) // 2 - _MAGNIFIER // 5, top[1])
    font = ImageFont.truetype('res/verdana.ttf', int(_MAGNIFIER * 0.7))
    draw.text(middle, text, font=font, fill='black')


def _draw_rectangle(draw, x, y):
    """ Draw a rectangle with the provided color in the given cell. """
    top, bot = _draw_box(x, y)
    draw.rectangle(top + bot, fill='white')


def _draw_cells(draw, width, height, puzzle):
    """ Draw all the cells on the puzzle. Since we start with a black
    background we do not need to draw the black cells without a number. """
    for x in range(width):
        for y in range(height):
            _draw_rectangle(draw, x, y)
            if puzzle[y][x] != None:
                _draw_text(draw, x, y, str(puzzle[y][x]))


def _draw_all(im, width, height, puzzle):
    """ Draw the image for the given puzzle. """
    draw = ImageDraw.Draw(im)

    _draw_background(draw)
    _draw_cells(draw, width, height, puzzle)


def draw(puzzle, filename, magnifier=None):
    """ Draw and save the image corresponding to the puzzle. """
    if magnifier is not None:
        global _MAGNIFIER
        _MAGNIFIER = magnifier

    width, height = len(puzzle[0]), len(puzzle)
    size = (width * _MAGNIFIER + _LINEWIDTH, height * _MAGNIFIER + _LINEWIDTH)

    im = Image.new("1", size)
    _draw_all(im, width, height, puzzle)
    im.save(filename + ".png")