
choices = []
#winner = False
for x in range (0, 9) :#array for tic tac toe all possible positions
    choices.append(str(x + 1))



def printBoard() :#Printing keyboad
    print( '\n -----')
    #print('n')
    print( '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print( ' -----')
    print( '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print( ' -----')
    print( '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print( ' -----\n')



    
def main():#main function when u want to refer the direct function name in terminal by just importing the code name 
    winner = False#basic codition
    i=0
    playerOneTurn = True
    while not winner :#until there is a winner the loop will continue
        printBoard()#basic board print after each move with updated move
        if(i>9):
            print("Its a Draw")
            exit(0)
        else:
            if playerOneTurn :#if this is true then player one turns
                print( "Player 1:")
                i+=1
            else :
                print( "Player 2:")
                i+=1

            try:
                choice = int(input(">> "))#if it is not an number it will go into except part
            except:
                print("please enter a valid field")
                continue#the program will continue
            if choices[choice - 1] == 'X' or choices [choice-1] == 'O':#this will not allow user to repeat the same position again
                print("illegal move, plase try again")
                continue

            if playerOneTurn :#placing each position with respective x and o
                choices[choice - 1] = 'X'
            else :
                choices[choice - 1] = 'O'

            playerOneTurn = not playerOneTurn#not inverses the boolean type each time 

            for x in range (0, 3) :#for checking the straight line if the straight lines match return winner
                y = x * 3
                if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) :
                    winner = True
                    printBoard()#taking a condition y=0 then it it will check 2 3 if y =1 then it will check 4 5 since it is multiplied by 3 in start 
                if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) :# for checking standing lines 
                    winner = True
                    printBoard()
    #now this part is for diagonal checking if they match diagonally
            if((choices[0] == choices[4] and choices[0] == choices[8]) or 
               (choices[2] == choices[4] and choices[4] == choices[6])) :
                winner = True
                printBoard()

    print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")
   #printing the winner
    
    
#if name == main is true means we are checkng if the namespace is main also we can run this program without putting main in it or checking this condition its just a pratice 
if __name__=='__main__':
    main()
else:
    print("loaded as module",__name__)        
        
