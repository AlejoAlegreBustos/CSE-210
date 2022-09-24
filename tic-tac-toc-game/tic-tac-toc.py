def main():
    print("Welcomte to Tic-Tac-Toe game")
    for i in range(0,9):
        if int(i) % 2 == 0:
            eleccion=int(input("It's player X's turn, choose a position from 0 to 9:"))
            grid("x", eleccion,int(i))
        elif int(i) % 2 != 0:
            eleccion=int(input("It's player O's turn, choose a position from 0 to 9:"))
            grid("o", eleccion,int(i))
    

def grid(choice, position,time):
    
    if int(time) == 0:
        p=[0,1,2,3,4,5,6,7,8,]
        for i in p:
            if i == position :
                if i != "x" or i != "o":
                    p[position]= choice

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

    else:
        for i in p:
            if i == position :
                if i != "x" or i != "o":
                    p[position]= choice

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
            
            checker=check_for_win(p, choice)
            if checker == True :
                print(f"felicitaciones juagdor {choice} has ganado")
                
                
            


def check_for_win(element_list, player):

    if element_list[0] == element_list[1] == element_list[2] == player or \
        element_list[3] == element_list[4] == element_list[5] == player or \
        element_list[6] == element_list[7] == element_list[8] == player:
        return True

    elif element_list[0] == element_list[3] == element_list[6] == player or \
        element_list[1] == element_list[4] == element_list[7] == player or \
        element_list[2] == element_list[5] == element_list[8] == player:
        return True

    elif element_list[0] == element_list[4] == element_list[8] == player or \
        element_list[2] == element_list[4] == element_list[7] == player:
        return True

    return False

main()
