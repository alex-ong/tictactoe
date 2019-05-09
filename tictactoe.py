class Board(object):
    def __init__(self):
        self.data = [["_" for i in range(3)] for j in range(3)]
    def copyOther(self, other):
        for i in range(3):
            for j in range(3):
                self.data[i][j] = other.data[i][j]
    
    def isWinner(self, player):
        other = self.otherPlayer(player)
        #check horizontal        
        for row in range(3):
            playerCount = 0
            otherCount = 0
            for col in range(3):
                if self.data[row][col] == player:
                    playerCount += 1
                elif self.data[row][col] == other:
                    otherCount += 1
            if playerCount == 3:
                return 1
            elif otherCount == 3:
                return -1
                
        #check vertical
        for col in range(3):
            playerCount = 0
            otherCount = 0
            for row in range(3):
                if self.data[row][col] == player:
                    playerCount += 1
                elif self.data[row][col] == other:
                    otherCount += 1
            if playerCount == 3:
                return 1
            elif otherCount == 3:
                return -1
        
        #diag one
        playerCount = 0
        otherCount = 0
        for i in range(3):
            if self.data[i][i] == player:
                playerCount += 1
            elif self.data[i][i] == other:
                otherCount += 1
        
        if playerCount == 3:
            return 1
        elif otherCount == 3:
            return -1

        #diag two
        playerCount = 0
        otherCount = 0
        for i in range(3):
            if self.data[i][2-i] == player:
                playerCount += 1
            elif self.data[i][2-i] == other:
                otherCount += 1
        
        if playerCount == 3:
            return 1
        elif otherCount == 3:
            return -1
        
        return 0
        
    def otherPlayer(self, player):
        if player == 'x':
            return 'o'
        else:
            return 'x'
            
    def validMoves(self):
        results = []
        for row in range(3):
            for col in range(3):
                if self.data[row][col] == "_":
                    results.append((row,col))
        return results
    
    def __str__(self):
        result = ""
        result += "    1    2    3\n"
        result += "a " + str(self.data[0]) + "\n"
        result += "b " + str(self.data[1]) + "\n"
        result += "c " + str(self.data[2]) + "\n"
        return result
    
    def finished(self):
        for row in range(3):
            for col in range(3):
                if self.data[row][col] == "_":
                    return False
        
        
        return True
        
def playerMove(b, current):
    valid = False
    while not valid:
        print (b)
        print (current + " to play: ")
        try: 
            col, row = raw_input().split()
            col = int(col) - 1
            row = ord(row) - ord('a')
        except:
            raise
        if 0 <= row <= 2 and 0 <= col <= 2:
            if b.data[row][col] == "_":
                b.data[row][col] = current
                valid = True

def aiMove(b, current):
    moveScores = []
    for move in b.validMoves():        
        row, col = move
        newBoard = Board()
        newBoard.copyOther(b)
        newBoard.data[row][col] = current
        gameOver = newBoard.isWinner(current)
        
        if gameOver != 0:
            moveScores.append([move,gameOver])
        elif not newBoard.finished():
            moveScores.append([move, -1 * aiMove(newBoard, newBoard.otherPlayer(current))[1]])
        else:
            moveScores.append([move, 0])
            
    moveScores.sort(key=lambda x: x[1], reverse=True)
    
    return moveScores[0]
    
        
if __name__ == '__main__':
    b = Board()
    current = 'o' #o starts

    while b.isWinner(current) == 0 and not b.finished():
        if current == 'x':
            current = 'o'
            playerMove(b, current)
        else:
            current = 'x'
            pos, score = aiMove(b,current)
            row, col = pos
            b.data[row][col] = current
    
    print(b)
    winner = b.isWinner(current)
    if winner == 1:        
        print (current + " is the winner")
    else:
        print "draw"
    