"""
File: babynames.py
Name: Roger(Yu-Ming) Chang
-----------------------------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
-----------------------------------------------------
This program will show a searching window for users
by entering baby names to search the change of ranks.
This program will only show the top 1,000 ranks, those
who ranked after 1,000 will be shown '*' instead.
"""

import tkinter as tk
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue', 'magenta']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    return GRAPH_MARGIN_SIZE + ((width - 2 * GRAPH_MARGIN_SIZE) / len(YEARS)) * year_index


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tk.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    for i in range(len(lookup_names)):
        years = []
        ranks = []
        coordinates = []

        # Decide which color will be used for a name.
        color = COLORS[i % len(COLORS)]

        if lookup_names[i] in name_data:
            # put year value and rank value in name_data to years_list[int] and ranks_list[int].
            for year, rank in sorted(name_data[lookup_names[i]].items()):
                years.append(int(year))
                ranks.append(int(rank))

            # Show 'name rank' on canvas.
            for year in YEARS:
                x = get_x_coordinate(CANVAS_WIDTH, YEARS.index(year)) + TEXT_DX
                # The name's rank in that year is within 1,000.
                if year in years:
                    y = ((CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK) * ranks[years.index(year)] \
                        + GRAPH_MARGIN_SIZE
                    canvas.create_text(x, y,
                                       text=lookup_names[i]+' '+str(ranks[years.index(year)]),
                                       anchor=tk.SW, fill=color)
                    coordinates.append((x, y))
                # The name's rank in that year is out of 1,000.
                else:
                    canvas.create_text(x, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                       text=lookup_names[i] + ' *',
                                       anchor=tk.SW, fill=color)
                    coordinates.append((x, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE))

            # Draw lines.
            for j in range(len(YEARS)-1):
                canvas.create_line(coordinates[j][0], coordinates[j][1],
                                   coordinates[j+1][0], coordinates[j+1][1],
                                   width=LINE_WIDTH, fill=color)


def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tk.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
