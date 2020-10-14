"""
File: breakout.py
Name: Roger(Yu-Ming) Chang
-----------------------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao
-----------------------------------------
This program is to create a breakout game,
each player has 3 chances to play until all bricks are eliminated.
Your game score will be presented in the upper left corner in the window.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3  # Chances to play the game before losing it.


def main():
    lives = NUM_LIVES
    graphics = BreakoutGraphics()

    # Animation
    while True:
        pause(FRAME_RATE)
        graphics.move_ball()
        graphics.wall_collisions()
        graphics.ball_collisions()
        if graphics.outside_window():
            graphics.reset_ball()
            lives -= 1
        # conditions for the end of the game.
        if lives == 0:
            graphics.game_over()
            break
        elif graphics.end_game():
            break


if __name__ == '__main__':
    main()
