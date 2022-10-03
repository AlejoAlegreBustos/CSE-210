import random


class Puzzle:
    """The person hiding from the Seeker. 

    The responsibility of Hider is to keep track of its location and distance from the seeker. 

    Attributes:
        _location (int): The location of the hider (1-1000).
        _distance (List[int]): The distance from the seeker.
    """
    # The puzzle is a secret word randomly chosen from a list.

    def __init__(self):
        """Constructs a new Hider.

        Args:
            self (Hider): An instance of Hider.
        """
        words = ["Dog",
                 "Puppy",
                 "Turtle",
                 "Rabbit",
                 "Parrot",
                 "Cat",
                 "Kitten",
                 "Goldfish",
                 "Mouse",
                 "Tropical fish",
                 "Hamster"]

        self._word = random.choice(words)
        self._guessed = True


    def get_hint(self):

        if self._distance[-1] == 0:
            hint = "(;.;) You found me!"
        elif self._distance[-1] > self._distance[-2]:
            hint = "(^.^) Getting colder!"
        elif self._distance[-1] < self._distance[-2]:
            hint = "(>.<) Getting warmer!"
        return hint

    def is_found(self):
        if self._word == self._guessed:
            return (self._distance[-1] == 0)

    def watch_seeker(self, seeker):
        """Watches the seeker by keeping track of how far away it is.

        Args:
            self (Hider): An instance of Hider.
        """
        distance = abs(self._location - seeker.get_location())
        self._distance.append(distance)

    def print_jumper(self,input_user):
        
        secret_word=self._word
        secret_word_listed=secret_word.split()
        for i in range(0,len(secret_word_listed)):
            print("_")
        
        for i in range(0,len(secret_word_listed)):
            counter=0
            if i==input_user:
                counter=0
                secret_word_listed[i]=input_user
                print(secret_word_listed)
                print("")
                for i in range(0,len(secret_word_listed) - counter):
                    print("_")
                print("")
                print("  /          /")
                print("    _____  ")
                print("  |       |   ")
                print("  |       |   ")
                print("   >> 0 <<")
                print("     -|-     ")
                print("     { } ")
                print("")

            else:
                counter+=1
                print(secret_word_listed)
                print("")
                for i in range(0,len(secret_word_listed) - counter):
                    print("_")
                print("  /          /")
                print("    _____  ")
                print("  |       |   ")
                print("  |       |   ")
                print("   >> 0 <<")
                print("     -|-     ")
                print("     { } ")
                print("")





        