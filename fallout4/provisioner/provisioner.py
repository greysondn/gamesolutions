from peewee import *

# ------------------------------------------------------------------------------
# Very naughty globals
# ------------------------------------------------------------------------------

database = SqliteDatabase(None)
# later... db.init(db_filepath, pragmas={'journal_mode': 'wal'})

# ------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------
class BaseModel(Model):
    '''
    Base model for database work. Just defines a database for usage later.
    '''
    class Meta:
        database = database
        
class Node(BaseModel):
    '''
    A location on our graph
    '''
    # primary key
    id      = AutoField(primary_key = True)
    
    # index in YAML file
    index = IntegerField()
    
    # name
    name = TextField()

    # x coordinate
    xPos = IntegerField()

    # y coordinate
    yPos = IntegerField()

class Solution(BaseModel):
    '''
    A solution for our problem
    '''
    # primary key
    id      = AutoField(primary_key = True)
    
    # nodes comprising the solution
    # by database key, not file key
    # gonna be json to text / json from text kinda solution.
    nodes   = TextField()
    
    # whether it's been checked yet
    checked = BooleanField()
    
    # length calculated for it
    length = FloatField()
    
# ------------------------------------------------------------------------------
# Module functions
# ------------------------------------------------------------------------------
def initDb(dbpath):
    database.init(dbpath, pragmas={'journal_mode': 'wal'})

def closeDb():
    database.close()

def createDb(dbpath):
    initDb(dbpath)
    
    with database as db:
        db.create_tables([Node, Solution])

