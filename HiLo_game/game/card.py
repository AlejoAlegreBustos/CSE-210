import random


# TODO: Implement the Die class as follows...

# 1) Add the class declaration. Use the following class comment.
"""A small cube with a different number of spots on each of its six sides.

The responsibility of Die is to keep track of the side facing up and calculate the points for 
it.

Attributes:
    value (int): The number of spots on the side facing up.
    points (int): The number of points the die is worth.
"""

class Card():

        def __init__(self):

            self.current_card=0
            self.next_card=0
            self.input_user=""
            self.points=0

        def random_card(self,guess_user):

            self.current_card=random.randint(1, 14)
            self.next_card=random.randint(1, 14)
            self.input_user=guess_user

            if self.next_card < self.current_card and self.input_user=="l" or self.next_card > self.current_card and self.input_user=="h" :
                self.points=+100
                return self.next_card
            elif self.next_card > self.current_card and self.input_user=="l" or self.next_card < self.current_card and self.input_user=="h":
                self.points=-75
                return self.next_card


