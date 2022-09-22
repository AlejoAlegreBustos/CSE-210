''' HiLo game'''

'''States

Higher_or_lower=""
User_input=""
Current_num=0

Behaviors

Random_num()
Input _verification()
Prin_results()'''

class HiLo():
 
    def init(self):
         
        self.score=300
        self.user_input=""
        self.current_num=0
        self.next_number=0

    def random_num(self):

        import random

        self.current_num=random.randint(1,13)

        return self.current_num

    def Input_verification(self, input_user):

        self.next_number=next(self.current_num)
        
        if self.current_num < self.next_number and input_user == "l":
            self.score = self.score + 75
        elif self.current_num > self.next_number and input_user == "h":
            self.score = self.score - 115

    def start_game():
        print("Welcome to HiLo game")
        
        random_num()