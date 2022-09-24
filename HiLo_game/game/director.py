from .card import Card


class Director:

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.card = 0
        self.guess_user=""
        self.is_playing = True
        self.score = 0
        self.total_score = 300


    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        guess_card = input("The next card will be higher o lower? [h/l]:  ")
        self.guess_user = guess_card

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        card=Card()
        self.card=card.random_card(self.guess_user)
        self.score += card.points
        self.total_score += self.score

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        value=self.card

        print(f"You card: {value}")
        print(f"Your score is: {self.total_score}\n")
        
        if self.score > 0:
            keep_playing= input("Would you like keep playing?[y/n]: ")
            if keep_playing == "y":
                self.is_playing = True
            else:
                self.is_playing = False
        else:
            self.is_playing = False