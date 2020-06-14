# TwilioQuest version 3.1.26
# Works in:
#    3.1.26

class Citizen():
    """
    A citizen of Python's Temple in TwilioQuest
    """
    
    greeting = "For the glory of Python!"
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name  = last_name
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"