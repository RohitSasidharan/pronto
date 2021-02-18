# Function to find shortest distance

class robot(object):
    def numMoves(input):
        x = 0
        y = 0
        movesList = input.split(',')
         
        # Traverse the instruction string
        
        for move in movesList:
                    
            if (move[0] == 'F'):
                x = x + int(move[1:])
 
            elif(move[0] == 'B'):
                x = x - int(move[1:])
 
            elif(move[0] == 'L'):
                y = y - int(move[1:])
 
            elif(move[0] == 'R'):
                y = y + int(move[1:])
        print("The minimum position required to go to the starting point is",abs((x)+(y)))  

#Get input from the user
controls=input("Enter the direction:");
robot.numMoves(controls)    
