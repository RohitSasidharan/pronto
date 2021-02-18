

# Function to find shortest distance 

def numMoves(input):
    countUp, countDown = 0, 0
    countLeft, countRight = 0, 0
    movesList = input.split(',')
    
    # traverse the instruction string
    
    for move in movesList:
        
        if (move[0] == 'F'):
            countUp = countUp + int(move[1:])
 
        elif(move[0] == 'B'):
            countDown = countDown + int(move[1:])
 
        elif(move[0] == 'L'):
            countLeft = countLeft + int(move[1:])
 
        elif(move[0] == 'R'):
            countRight = countRight + int(move[1:])
    print("Final Position: ", (abs(countRight - countLeft)+abs(countUp - countDown)))  
    

#Get input from the user
control=input("Enter the direction:");
print(control)
numMoves(control)
