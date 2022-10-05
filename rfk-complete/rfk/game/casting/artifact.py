from game.casting.actor import Actor
import random

# # TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
# Several artifacts are randomly positioned on the screen.
# Each artifact has a randomly chosen symbol and message.


class Artifact(Actor):

    def __init__(self):
        self._position= super().__init__()
        self._artifact_element=""
        self.message=""

    def set_position(self, position):
        """Updates the position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position

    
    def set_message(self,message):
        self._message=message

    def get_message(self):
        """Gets the actor's textual representation.
        
        Returns:
            string: The actor's textual representation.
        """
        return self._message

    def set_text(self,text):
        self._text= text

    def get_text(self):
        """Gets the actor's textual representation.
        
        Returns:
            string: The actor's textual representation.
        """
        return self._text


    def set_font_size(self,font_size):
        self._font_size=font_size


    def get_font_size(self):

        return self._font_size

    def set_color(self, color):
        """Updates the color to the given one.
        
        Args:
            color (Color): The given color.
        """
        self._color = color

    def get_color(self):
        """Gets the actor's color as a tuple of three ints (r, g, b).
        
        Returns:
            Color: The actor's text color.
        """
        return self._color


    def move_next(self, max_x, max_y):
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)