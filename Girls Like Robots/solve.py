from enum import Enum
from itertools import permutations
from tqdm import tqdm
import asyncio as aio

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
        
    def __repr__(self):
        return str(self.ttype.value)

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
        
        successes = [
            TokenType.EMPTY,
            TokenType.EXPANDABLE
        ]

        if (self.ttype in successes):
            ret = True
        
        return ret

    def hasToken(self):
        ret = True
        
        failures = [
            TokenType.EDGE,
            TokenType.EMPTY,
            TokenType.EXPANDABLE
        ]
        
        if (self.ttype in failures):
            ret = False
        
        return ret
    
    def isExpandable(self):
        ret = False
        
        successes = [
            TokenType.EMPTY
        ]
        
        if (self.ttype in successes):
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

class TokenPlacementError(Exception):
    '''
    Signifies that an error happened during token placement, generally meaning
    that a token placement is invalid.
    '''
    def __init__(self, *args):
        super().__init__(args)

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
        
        self.seenBoards:list[str] = []
    
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
        strRep:str = str(tokens)
        
        if (strRep) in self.seenBoards:
            raise TokenPlacementError()
        else:
            self.seenBoards.append(strRep)
        
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
                if (board[y][x].hasToken()):
                    # we can expand in every direction, actually
                    #
                    # north
                    if (y - 1 >= 0):
                        if (board[y-1][x].isExpandable()):
                            board[y-1][x] = Expandable()
                    
                    # south
                    if ((y + 1) < bHeight):
                        if (board[y+1][x].isExpandable()):
                            board[y+1][x] = Expandable()
                    
                    # West
                    if ((x - 1) >= 0):
                        if (board[y][x-1].isExpandable()):
                            board[y][x-1] = Expandable()
                            
                    # East
                    if ((x + 1) < bWidth):
                        if (board[y][x+1].isExpandable()):
                            board[y][x+1] = Expandable()
                
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
        
        placedToken = False
        failure     = False
        carryOn     = True
        
        while carryOn:
            # current token
            curToken = chkBag.pop(0)
            self.markViableSpots(secondBoard)
            
            for y in range(len(secondBoard)):
                for x in range(len(secondBoard[0])):
                    if not placedToken:
                        if (secondBoard[y][x].ttype == TokenType.EXPANDABLE):
                            if (self.state[y][x].ttype == curToken.ttype):
                                secondBoard[y][x] = curToken
                                placedToken = True
            
            # gate conditions
            if (not placedToken):
                carryOn = False
                failure = True
            if (len(chkBag) == 0):
                carryOn = False
        
        # that's it.
        if (failure):
            raise TokenPlacementError()
    
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
        
        # count the number of permutations
        totIterations:int = 1

        for x in range(len(toks)):
            totIterations = totIterations * (x + 1)
        
        for permutation in tqdm(
                                iterable = permutations(toks),
                                total = totIterations
            ):
            
            if (not solved):
                # place tokens and score
                validPlacement = True
                try:
                    self.place(list(permutation))
                except TokenPlacementError:
                    validPlacement = False

                if validPlacement:
                    score = self.score()
                    
                    # check for better score
                    if (score > self.bestScore):
                        self.bestBoard = self.toStr()
                        self.bestScore = score
                        
                    # check for target score
                    if (target != None):
                        if (self.bestScore >= target):
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

def solve_1_2_5():
    # first real puzzle of the game, yo
    start:list[list[Token]] = [
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
        Robot(),
        Robot(),
        Robot(),
        Robot(),
        Robot()
    ]
    
    board.addBag(bag)
    
    board.solve(26)
    
def solve_1_3_3():
    # Don't panic these Robots!
    start:list[list[Token]] = [
        [Empty(), Empty(), Empty()],
        [Empty(), Empty(), Empty()],
        [Empty(), Empty(), Empty()]
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
        Robot()
    ]
    
    board.addBag(bag)
    
    board.solve(12)
    
def solve_1_3_4():
    start:list[list[Token]] = [
        [Empty(), Empty(), Empty()],
        [Empty(), Empty(), Empty()],
        [Empty(), Empty(), Empty()]
    ]
    
    board:Board = Board(start)
    
    bag:list[Token] = [
        Girl(),
        Girl(),
        Girl(),
        Girl(),
        Girl(),
        Nerd(),
        Nerd(),
        Nerd(),
        Nerd()
    ]
    
    board.addBag(bag)
    
    board.solve(8)

def solve_1_3_4_test():
    # variant to help test hard mode placement.
    start:list[list[Token]] = [
        [Nerd(), Empty(), Empty()],
        [Empty(), Empty(), Empty()],
        [Empty(), Empty(), Empty()]
    ]
    
    board:Board = Board(start)
    
    bag:list[Token] = [
        Girl(),
        Nerd(),
        Girl(),
        Nerd(),
        Girl(),
        Nerd(),
        Girl(),
        Girl()
    ]
    
    board.addBag(bag)
    
    board.forcedBagOrder           = True
    board.forcedBagOrderBag        = bag
    
    board.placementExpandsOutwards = True
    
    board.solve(8)

def solve_1_3_6():
    # Sometimes you don't get to pick who to place next!
    start:list[list[Token]] = [
        [Empty(), Empty()],
        [Empty(), Empty()],
        [Empty(), Empty()]
    ]
    
    board:Board = Board(start)
    
    bag:list[Token] = [
        Girl(),
        Robot(),
        Girl(),
        Girl(),
        Robot(),
        Robot()
    ]
    
    board.addBag(bag)
    
    board.forcedBagOrder    = True
    board.forcedBagOrderBag = bag
    
    board.solve(14)

def solve_1_4_5():
    # the ladies would like Dave to know he's cheesy
    start:list[list[Token]] =[
        [Empty(), Empty(), Empty(), Nerd() ],
        [Empty(), Empty(), Empty(), Empty()],
        [Robot(), Empty(), Empty(), Empty()]
    ]
    
    board:Board = Board(start)
    
    bag:list[Token] = [
        Robot(),
        Girl(),
        Nerd(),
        Girl(),
        Girl(),
        Robot(),
        Robot(),
        Nerd(),
        Girl(),
        Girl()
    ]
    
    board.addBag(bag)
    
    board.placementExpandsOutwards = True
    board.forcedBagOrder           = True
    board.forcedBagOrderBag        = bag
    
    board.solve(25)

def solve_1_3_7():
    start:list[list[Token]] = [
        [Nerd(),  Empty(), Empty()],
        [Empty(), Empty(), Empty()],
        [Empty(), Empty(), Empty()]
    ]
    
    board:Board = Board(start)
    
    bag:list[Token] = [
        Robot(),
        Girl(),
        Robot(),
        Robot(),
        Girl(),
        Girl(),
        Girl(),
        Girl()
    ]
    
    board.addBag(bag)
    
    board.forcedBagOrder    = True
    board.forcedBagOrderBag = bag

    board.placementExpandsOutwards = True
    
    board.solve(18)

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
        Robot(),
        Girl(),
        Robot(),
        Robot(),
        Nerd(),
        Girl(),
        Girl(),
        Nerd(),
        Nerd(),
        Girl(),
        Nerd(),
        Nerd(),
        Robot(),
        Robot(),
        Girl(),
        Nerd(),
        Girl(),
        Robot(),
        Girl()
    ]
    
    board.addBag(bag)
    
    board.forcedBagOrder           = True
    board.forcedBagOrderBag        = bag
    board.placementExpandsOutwards = True
    
    board.solve(40)
################################################################################
async def main():
    # solve_1_2_5()      # solves
    # solve_1_3_3()      # solves
    # solve_1_3_4()      # solves
    # solve_1_3_6()      # solves
    # solve_1_3_4_test() # solves
    # solve_1_3_7()      # solves
    solve_1_4_6()

if (__name__ == "__main__"):
   aio.run(main())