# TODO: Implement the Seeker class as follows...

# 1) Add the class declaration. Use the following class comment.
class Jumper():

    def __init__(self):
        self._letter = ""

    def get_letter(self):

        return self._letter



    def change_letter(self, new_letter):
        """Moves to the given location.
        Args:
            self (Seeker): An instance of Seeker.
            location (int): The given location.
        """
        self._letter=new_letter
