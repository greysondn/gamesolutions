from enum import Enum

class TokenType(Enum):
    EMPTY      = "_"
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
        
        return ret

    def getMood(self, neighbors:list[TokenType]) -> int:
        ret = self.basicMood(neighbors)
        return ret

class Girl(Token):
    def __init__(self):
        super().__init__(TokenType.GIRL)
        
        self.feelings[TokenType.ROBOT] = 1

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
        
        self.feelings[TokenType.EDGE] =  1
        self.feelings[TokenType.NERD] = -1
        
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

class Board():
    def __init__(self, state:list[list[Token]]):
        self.core:list[list[Token]]  = state
        self.state:list[list[Token]] = []
        self.initFromCore()
        
        self.bestBoard:list[list[Token]] = []
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
        for i in range(len(self.state)):
            swp_r:list[Token] = []
            swp_r.append(Edge())
            
            row = self.state[i]
            
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
                if (x.ttype == TokenType.EMPTY):
                    ret = ret + 1
        
        return ret
    
    def place(self, tokens:list[Token]):
        for y in range(len(self.state)):
            for x in range(len(self.state[0])):
                if (self.state[y][x].ttype == TokenType.EMPTY):
                    self.state[y][x] = tokens.pop(0)
    
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