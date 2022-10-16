from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here! 

class MoveActorsAction(Action):
    
# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each acto

    def __init__(self):
        self.actors=[]

    def execute(self, cast, script):
        self.actors.append(cast.)
