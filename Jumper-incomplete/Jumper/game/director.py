from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        # self._hider = Hider()
        self._puzzler = Puzzle()
        self._is_playing = True
        self._word =""
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        
        new_letter = self._terminal_service.read_text("\nEnter a letter: ")
        self._jumper.change_letter(new_letter)
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        #listo la palabra
        "checkeo letra"
        self._word=self._puzzler.get_word()
        # self._puzzler.check_letter(self._word, self._jumper._letter)
        word_listed=self._puzzler.listing_word(self._word)
        #checkeo letra me devuelve true o false para dibujar
        self._puzzler.cartoonist(self._puzzler.check_letter(self._word, self._jumper._letter), word_listed,self._jumper._letter)

        
        
    def _do_outputs(self):

        is_alive = self._puzzler.complete_word_checker(self._puzzler.word_listed_)
        
        if is_alive == True:
            self._is_playing = True
        else:
            self._is_playing = False
            self._terminal_service.write_text("you don't complete de word")