# """este sera un proyecto  de tateti"""

# def main():
#     print("Welcomte to Tic-Tac-Toe game")

    

# def take_decision(ptn):

#     "this function will take the decision of the user"
#     position=int(ptn)

#     return position


def grid(choice, position):

    p=[0,1,2,3,4,5,6,7,8,]
    

    print("\n")
    print("\t       |        |")
    print(f"\t    {p[0]}  |    {p[1]}   |  {p[2]} ")
    print('\t   ____|________|_____')
 
    print("\t       |        |")
    print(f"\t    {p[3]}  |    {p[4]}   |  {p[5]} ")
    print('\t   ____|________|_____')
 
    print("\t       |        |")
 
    print(f"\t    {p[6]}  |    {p[7]}   |  {p[8]} ")
    print("\t       |        |")
    print("\n")

    for i in p:
        if i == position and i != "x" or i != "o":
            p[position]= choice
            
        


grid("x",5)