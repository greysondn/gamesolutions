from enum import Enum
from itertools import permutations
from tqdm import tqdm

class TokenType(Enum):
    EMPTY      = "_"
    EXPANDABLE = "?"
    ALIEN_GIRL = "Q"
    ALIEN_NERD = "Z"
    BEN        = "B"
    BUS_DRIVER = "D"
    COW        = "C"
    GIRL       = "G"
    HOBOBOT    = "H"
    JUNE       = "J"
    M_BOT      = "M"
    NERD       = "N"
    ROBOT      = "R"
    SPACE_SEAL = "S"
    TRAIN_GIRL = "X"
    TRAIN_NERD = "Y"
    EDGE       = "E"

class Token():
    def __init__(self, ttype:TokenType):
        self.ttype:TokenType = ttype
        self.feelings:dict[TokenType,int] = {}
        
    def basicMood(self, neighbors:list[TokenType]) -> int:
        ret = 0
        
        for neighbor in neighbors:
            ret = ret + self.feelings.get(neighbor, 0)
        
        if (ret < 0):
            ret = 0
        
        return ret

    def getMood(self, neighbors:list[TokenType]) -> int:
        ret = self.basicMood(neighbors)
        return ret
    
    def isEmpty(self):
        ret = False

        if (self.ttype == TokenType.EMPTY):
            ret = True
        elif (self.ttype == TokenType.EXPANDABLE):
            ret = True
        
        return ret

class Girl(Token):
    def __init__(self):
        super().__init__(TokenType.GIRL)
        
        self.feelings[TokenType.NERD]  = -1
        self.feelings[TokenType.ROBOT] =  1

class Robot(Token):
    def __init__(self):
        super().__init__(TokenType.ROBOT)
        
        self.feelings[TokenType.GIRL] = 1
        
    def getMood(self, neighbors:list[TokenType]) -> int:
        ret = self.basicMood(neighbors)
        
        # robots freak out if surrounded by girls
        if (neighbors.count(TokenType.GIRL) == 4):
            ret = 0
        
        return ret

class Nerd(Token):
    def __init__(self):
        super().__init__(TokenType.NERD)
        
        self.feelings[TokenType.EDGE]  =  1
        self.feelings[TokenType.GIRL]  =  1
        self.feelings[TokenType.NERD]  = -1
        self.feelings[TokenType.ROBOT] =  1
        
class AlienGirl(Token):
    def __init__(self):
        super().__init__(TokenType.ALIEN_GIRL)

class AlienNerd(Token):
    def __init__(self):
        super().__init__(TokenType.ALIEN_NERD)

class Ben(Token):
    def __init__(self):
        super().__init__(TokenType.BEN)

class Edge(Token):
    def __init__(self):
        super().__init__(TokenType.EDGE)

class Empty(Token):
    def __init__(self):
        super().__init__(TokenType.EMPTY)

class Expandable(Token):
    def __init__(self):
        super().__init__(TokenType.EXPANDABLE)

class Board():
    def __init__(self, state:list[list[Token]]):
        self.core:list[list[Token]]        = state
        self.state:list[list[Token]]       = []
        self.tokensToPlace:list[Token]     = []
        self.forcedBagOrder                = False
        self.forcedBagOrderBag:list[Token] = []
        self.placementExpandsOutwards      = False
        self.initFromCore()
        
        self.bestBoard:str               = ""
        self.bestScore:int               = 0
    
    def initFromCore(self):
        # creating our state is a pain
        swp_width  = len(self.core[0]) + 2
        
        self.state:list[list[Token]] = []
        
        # first row
        swp_a:list[Token] = []
        
        for x in range(swp_width):
            swp_a.append(Edge())
        
        self.state.append(swp_a)
        
        # middle rows
        for i in range(len(self.core)):
            swp_r:list[Token] = []
            swp_r.append(Edge())
            
            row = self.core[i]
            
            for j in range(len(row)):
                swp_r.append(row[j])
            
            swp_r.append(Edge())
            self.state.append(swp_r)
        
        # last row
        swp_z:list[Token] = []
        
        for x in range(swp_width):
            swp_z.append(Edge())
        
        self.state.append(swp_z)
    
    def score(self):
        ret = 0
        for x in range(1, (len(self.state[0]) - 1)):
            for y in range(1, (len(self.state) -1)):
                neighbors:list[TokenType] = []
                neighbors.append(self.state[y - 1][x].ttype)
                neighbors.append(self.state[y + 1][x].ttype)
                neighbors.append(self.state[y][x - 1].ttype)
                neighbors.append(self.state[y][x + 1].ttype)

                ret = ret + self.state[y][x].getMood(neighbors)
        return ret
    
    def countEmptySpaces(self):
        ret = 0
        
        for y in self.state:
            for x in y:
                if (x.isEmpty()):
                    ret = ret + 1
        
        return ret
    
    def place(self, tokens:list[Token]):
        if self.placementExpandsOutwards:
            if self.forcedBagOrder:
                self.placeHardMode(tokens)
        else:
            self.placeFast(tokens)

    def placeFast(self, tokens:list[Token]):
        for y in range(len(self.state)):
            for x in range(len(self.state[0])):
                if (self.state[y][x].ttype == TokenType.EMPTY):
                    self.state[y][x] = tokens.pop(0)
    
    def markViableSpots(self, board:list[list[Token]]):
        bHeight = len(board)
        bWidth  = len(board[0])
        for y in range(bHeight):
            for x in range(bWidth):
                # check for empty or viable
                if (not board[y][x].isEmpty()):
                    # we can expand in every direction, actually
                    #
                    # north
                    if (y - 1 >= 0):
                        if (board[y-1][x].isEmpty()):
                            board[y-1][x] = Expandable()
                
    def placeHardMode(self, tokens:list[Token]):
        # hard mode is defined as:
        # forced bag order
        # placement expands outwards
        
        # need a clone of the board
        secondBoard = self.state.copy()
        self.initFromCore()
        
        # now, the question is if we can place the tokens in the given positions
        # such that we end up with a valid board state.
        
        # I think the easiest way is to just place the tokens on the board
        self.placeFast(tokens)
        
        # and then check it
        chkBag = self.forcedBagOrderBag.copy()
        
        curToken = chkBag.pop(0)
    
    def addBag(self, bag:list[Token]):
        for token in bag:
            self.tokensToPlace.append(token)
    
    def toStr(self):
        ret = ""
        for row in self.state:
            for cell in row:
                ret = ret + str(cell.ttype.value)
            ret = ret + "\n"
        return ret
                    
    def solve(self, target=None):
        # build a token bag
        blankCount:int = self.countEmptySpaces() - len(self.tokensToPlace)
        toks:list[Token] = self.tokensToPlace.copy()
        for i in range(blankCount):
            toks.append(Empty())
            
        # we solve this by permutating the token bag,
        # placing the tokens,
        # scoring it,
        # and then moving on.
        # If there is a target score, we can stop when we hit it.
        solved:bool = False
        self.bestScore = 0
        self.bestBoard = ""
        self.initFromCore()
        
        for permutation in tqdm(permutations(toks)):
            if (not solved):
                # place tokens and score
                self.place(list(permutation))
                score = self.score()
                
                # check for better score
                if (score > self.bestScore):
                    self.bestBoard = self.toStr()
                    self.bestScore = score
                    
                # check for target score
                if (target != None):
                    if (self.bestScore > target):
                        solved = True
                
                # reset
                self.initFromCore()
        
        
        # print best at end
        print("-------------------------------------")
        print(self.bestScore)
        print(self.bestBoard)
        print("-------------------------------------")
                

        
        
    
'''
    BUS_DRIVER = "D"
    COW        = "C"
    GIRL       = "G"
    HOBOBOT    = "H"
    JUNE       = "J"
    M_BOT      = "M"
    NERD       = "N"
    ROBOT      = "R"
    SPACE_SEAL = "S"
    TRAIN_GIRL = "X"
    TRAIN_NERD = "Y"
'''


def solve_1_4_5():
    # the ladies would like Dave to know he's cheesy
    start:list[list[Token]] =[
        [Empty(), Empty(), Empty(), Nerd() ],
        [Empty(), Empty(), Empty(), Empty()],
        [Robot(), Empty(), Empty(), Empty()]
    ]
    
    board:Board = Board(start)
    
    bag:list[Token] = [
        Girl(),
        Girl(),
        Girl(),
        Girl(),
        Girl(),
        Robot(),
        Robot(),
        Robot(),
        Nerd(),
        Nerd()
    ]
    
    board.addBag(bag)
    
    board.solve(25)

def solve_1_4_6():
    # Are you sure that's a regulation size chicken?
    start:list[list[Token]] =[
        [Empty(), Empty(), Empty(), Empty(), Empty()],
        [Empty(), Empty(), Empty(), Robot(), Empty()],
        [Empty(), Empty(), Empty(), Empty(), Empty()],
        [Empty(), Empty(), Empty(), Empty(), Empty()],
        [Empty(), Empty(), Empty(), Empty(), Empty()]
    ]
    
    board:Board = Board(start)
    
    bag:list[Token] = [
        Girl(),
        Girl(),
        Girl(),
        Girl(),
        Girl(),
        Girl(),
        Girl(),
        Robot(),
        Robot(),
        Robot(),
        Robot(),
        Robot(),
        Robot(),
        Nerd(),
        Nerd(),
        Nerd(),
        Nerd(),
        Nerd(),
        Nerd()
    ]
    
    board.addBag(bag)
    
    board.solve(40)
################################################################################
if (__name__ == "__main__"):
    solve_1_4_6()