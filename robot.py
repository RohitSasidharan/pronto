
def numMoves(input):
    x = 0
    y = 0
    movesList = input.split(',')
    for move in movesList:
        
        if (move[0] == 'F'):
            x = x + int(move[1:])
 
        elif(move[0] == 'B'):
            x = x - int(move[1:])
 
        elif(move[0] == 'L'):
            y = y - int(move[1:])
 
        elif(move[0] == 'R'):
            y = y + int(move[1:])
    print(abs((x)+(y)))  
    
#Get input from the user
control=input("Enter the direction:");
print(control)
numMoves(control)

