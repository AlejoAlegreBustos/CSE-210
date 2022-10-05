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

    def index_word(self,input_user):
        word=self._word
        index=word.find(input_user)
        return index


    def counter(self,true_or_false):
        number=-1
        if true_or_false == False:
            number=number + 1
            return number
        else:
            pass
    
    def check_letter(self,word_listed,input_user):
        var=False
        try:
            index=word_listed.index(input_user)
            for i in range(0,len(word_listed)):
                if input_user == word_listed[index]:
                    var= True
                    break
                else:
                    var= False
        except:
            return var
    def listing_word(self,word):
        
        secret_word=word
        secret_word2=secret_word
        secret_word_listed=list(secret_word2.strip())
        for i in range(0,len(secret_word_listed)):
            secret_word_listed[i]="_"
        return secret_word_listed


    def cartoonist(self,letter_true_or_false,list_word,input_user):
        parachute=["______","|","|","______"]
        if letter_true_or_false==True:
            index_word_replace=self.index_word(input_user)
            list_word[index_word_replace]=input_user
            print("")
            print(parachute[0])
            print(f"  {parachute[1]}          {parachute[2]}")
            print({parachute[3]})
            print("  |       |   ")
            print("  |       |   ")
            print("   >> 0 <<")
            print("     -|-     ")
            print("     { } ")
            print("")
            print(secret_word_listed)
        else:
            contador=self.counter(letter_true_or_false)
            parachute[contador]=""
            print("")
            print(parachute[0])
            print(f"  {parachute[1]}          {parachute[2]}")
            print({parachute[3]})
            print("  |       |   ")
            print("  |       |   ")
            print("   >> 0 <<")
            print("     -|-     ")
            print("     { } ")
            print("")



      



        