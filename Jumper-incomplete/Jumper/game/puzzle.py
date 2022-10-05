import random

class Puzzle:
    # The puzzle is a secret word randomly chosen from a list.

    def __init__(self):
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
        self._guessed = False
      
    def complete_word_checker(self,word_in_list):
        for letter in word_in_list:
            if letter != "_": 
               self._guessed=True
        if self._guessed == True:
            return True
        else:
            return False

    def get_word(self):

        return self._word

    def print_jumper(self,input_user):
        
        secret_word=self.get_word()
        secret_word_listed=list(secret_word.strip())
        for i in range(0,len(secret_word_listed)):
            secret_word_listed[i]="_"
        print(secret_word_listed)

        lettercount=len(secret_word_listed)
        counter=0
        while lettercount >> counter:

            check_or_not=self.complete_word_checker(secret_word_listed)
            if check_or_not==True:
                print(secret_word_listed)
                print("you win")
                break 
            else:    
                if i==input_user:
                    secret_word_listed[i]=input_user
                    print(secret_word_listed)
                    print("")
                    print("      ______ ")
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
                    print("")

                    print("      ______   ")
                    print("  /          /")
                    print("    _____  ")
                    for i in range(0,len(secret_word_listed) - counter):
                        print("  |       |   ")
                    print("   >> 0 <<")
                    print("     -|-     ")
                    print("     { } ")
                    print("")

        




        