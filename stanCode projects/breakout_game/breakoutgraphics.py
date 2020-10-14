"""
File: breakout.py
Name: Roger(Yu-Ming) Chang
-----------------------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao
-----------------------------------------
Provide vary methods that may be helpful to build a breakout game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (window_width-paddle_width)/2, window_height-paddle_offset)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Create a scoreboard.
        self.__score = 0
        self.__board = GLabel('Score: ' + str(self.__score))
        self.__board.font = '-30'
        self.window.add(self.__board, 0, self.__board.height+5)

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0
        self.reverse_dy = -INITIAL_Y_SPEED

        # Initialize our mouse listeners.
        onmousemoved(self.move_paddle)
        onmouseclicked(self.click_to_start)
        self.__start = False

        # Draw bricks.
        self.__count = 0
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.__brick = GRect(brick_width, brick_height)
                self.__brick.filled = True

                if i // 2 == 0:
                    self.__brick.fill_color = 'red'
                    self.__brick.color = 'red'
                if i // 2 == 1:
                    self.__brick.fill_color = 'orange'
                    self.__brick.color = 'orange'
                if i // 2 == 2:
                    self.__brick.fill_color = 'yellow'
                    self.__brick.color = 'yellow'
                if i // 2 == 3:
                    self.__brick.fill_color = 'green'
                    self.__brick.color = 'green'
                if i // 2 == 4:
                    self.__brick.fill_color = 'blue'
                    self.__brick.color = 'blue'

                brick_y = brick_offset + (brick_height + brick_spacing) * i
                brick_x = (brick_width + brick_spacing) * j

                self.window.add(self.__brick, brick_x, brick_y)
                self.__count += 1

    def move_paddle(self, mouse):
        """
        Set the paddle to move horizontally with mouse moved and is contained in window.

        Input:
            event (GMouseEvent): mouse moved event
        """
        self.paddle.x = mouse.x - self.paddle.width / 2
        if self.paddle.x <= 0:
            self.paddle.x = 0
        if self.paddle.x + self.paddle.width >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width

    def click_to_start(self, event):
        """
        Start the game if the mouse is clicked and detect whether the game is started.

        Input:
            event (GMouseEvents): mouse clicked event
        """
        if not self.__start:
            self.set_ball_direction()
            self.__start = True

    def set_ball_direction(self):
        """
        Give ball x, y velocity which will determine its initial direction.
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def get_x_velocity(self):
        """
        Return ball x velocity.
        """
        return self.__dx

    def get_y_velocity(self):
        """
        Return ball y velocity.
        """
        return self.__dy

    def move_ball(self):
        """
        Move ball by the change in x and the change in y stored in class BreakoutGraphics.
        """
        self.ball.move(self.__dx, self.__dy)

    def wall_collisions(self):
        """
        Update dx and dy depending on whether the ball has hit walls.
        """
        if 0 >= self.ball.x or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        if 0 >= self.ball.y:
            self.__dy = -self.__dy

    def ball_collisions(self):
        """
        Remove bricks and change ball's direction when the ball hit bricks.
        Rebound the ball by changing its y velocity when the ball hit the paddle.
        The score will add one when each time brick was removed.
        """
        up_l_corner = self.window.get_object_at(self.ball.x, self.ball.y)
        up_r_corner = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        down_l_corner = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        down_r_corner = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)

        # The situation that the ball hits the paddle.
        if down_l_corner == self.paddle:
            self.__dy = self.reverse_dy
        elif down_r_corner == self.paddle:
            self.__dy = self.reverse_dy

        # The situation that the ball hits bricks and remove them.
        if up_l_corner is not None and up_l_corner is not self.paddle and up_l_corner is not self.__board:
            self.__dy = -self.__dy
            self.window.remove(up_l_corner)
            self.__count -= 1
            self.__score += 1
            self.__board.text = 'Score: ' + str(self.__score)
        elif up_r_corner is not None and up_r_corner is not self.paddle and up_r_corner is not self.__board:
            self.__dy = -self.__dy
            self.window.remove(up_r_corner)
            self.__count -= 1
            self.__score += 1
            self.__board.text = 'Score: ' + str(self.__score)
        elif down_l_corner is not None and down_l_corner is not self.paddle and down_l_corner is not self.__board:
            self.__dy = -self.__dy
            self.window.remove(down_l_corner)
            self.__count -= 1
            self.__score += 1
            self.__board.text = 'Score: ' + str(self.__score)
        elif down_r_corner is not None and down_r_corner is not self.paddle and down_r_corner is not self.__board:
            self.__dy = -self.__dy
            self.window.remove(down_r_corner)
            self.__count -= 1
            self.__score += 1
            self.__board.text = 'Score: ' + str(self.__score)

    def outside_window(self):
        """
        Check whether the ball has fallen outside the window bottom.
        :return: Bool
        """
        if self.ball.y >= self.window.height:
            return True

    def reset_ball(self):
        """
        Reset the ball's location and velocity after the ball has fallen outside the window.
        :return: Bool
        """
        self.window.remove(self.ball)
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self.__dx = 0
        self.__dy = 0
        self.window.add(self.ball)
        self.__start = False

    def game_over(self):
        """
        One of the conditions for game over. When all chances were used out.
        """
        self.reset_ball()
        lose = GLabel('You lose!')
        lose.font = '-70-bold'
        self.window.add(lose, (self.window.width-lose.width)/2, 500)

    def end_game(self):
        """
        One of the conditions for game over. When all bricks were remove.
        :return: Bool
        """
        if self.__count == 0:
            self.window.remove(self.ball)
            congrats = GLabel('Congratulation!')
            congrats.font = '-70-bold'
            congrats.color = 'red'
            self.window.add(congrats, (self.window.width-congrats.width)/2, 500)
            return True






