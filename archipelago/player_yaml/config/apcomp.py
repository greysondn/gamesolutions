from random import choice
from typing import Any

"""A series of basic components to make apconfigs out of.
"""

class ApComp():
    def __init__(self, name:str, default:Any=None, indent:int=0):
        self.name:str   = name
        '''The name of this field in the config yaml'''
        self.indent:int = indent
        '''The number of spaces to indent this when printing it'''
        self.value:Any = default
        '''The current value of this component. This should be overridden with
           a type in child classes.'''
    
    def __repr__(self) -> str:
        """Override this to give a correct string representation of this object

        Returns:
            str: representation of this object
        """
        ret:str = ""
        
        ret = ret + f"{' ' * self.indent}"
        ret = ret + f"{self.name}: {self.value}"
        
        return ret

    def set(self, value:Any) -> None:
        """Override this to provide a way to set this component's value with
           some basic checking or whatever

        Args:
            value (Any): Value to set this component to
        """
        self.value = value
    
    def get(self) -> Any:
        """Override this to provide a way to retrieve this component's value

        Returns:
            Any: this component's value
        """
        return self.value

# ------------------------------------------------------------------------------

class BoolComp(ApComp):
    def __init__(self, name:str, default:bool, indent:int=0, outputStrings:list[str]=["true", "false"]):
        # parent
        super().__init__(name, default, indent)
        
        # tweaks
        self.value:bool = default
        """The current value of this component."""
        self.outputStrings:list[str] = outputStrings
        """A short list [true, false] of strings to output for the values of this component"""

    def __repr__(self) -> str:
        ret:str = ""
        
        ret = ret + f"{' ' * self.indent}"
        ret = ret + f"{self.name}: "
        
        if (self.value):
            ret = ret + f'"{self.outputStrings[0]}"'
        else:
            ret = ret + f'"{self.outputStrings[1]}"'
        
        return ret

    def set(self, value:bool) -> None:
        self.value = value
        
    def get(self) -> bool:
        return self.value

class IntComp(ApComp):
    def __init__(self, name:str, default:int, indent:int=0):
        # parent
        super().__init__(name, default, indent)
        
        # tweaks
        self.value:int = default
        """The current value of this component."""

    def __repr__(self) -> str:
        ret:str = ""
        
        ret = ret + f"{' ' * self.indent}"
        ret = ret + f"{self.name}: {self.value}"
                
        return ret

    def set(self, value:int) -> None:
        self.value = value
        
    def get(self) -> int:
        return self.value

class StrComp(ApComp):
    def __init__(self, name:str, default:str, indent:int=0):
        # parent
        super().__init__(name, default, indent)
        
        # tweaks
        self.value:str = default
        """The current value of this component."""

    def __repr__(self) -> str:
        ret:str = ""
        
        ret = ret + f"{' ' * self.indent}"
        ret = ret + f'{self.name}: "{self.value}"'
                
        return ret

    def set(self, value:str) -> None:
        self.value = value
        
    def get(self) -> str:
        return self.value

class StrEnumComp(StrComp):
    def __init__(self, name:str, default:str, validValues:list[str], indent:int=0):
        # parent
        super().__init__(name, default, indent)
        
        # tweaks
        self.validValues:list[str] = validValues
        """valid values for this to be set to"""
        
        # go ahead and set that value again just so it gets validated
        self.set(default)
        
    def set(self, value:str) -> None:
        if (value in self.validValues):
            self.value = value
        else:
            raise ValueError()

class StrEnumRandomizableComp(StrEnumComp):
    # so this is identical to parent, except it also allows the usage of
    # "random" as a value and provides handling for that value
    def set(self, value:str) -> None:
        if (value in self.validValues):
            self.value = value
        elif (value.lower() == "random"):
            self.set(choice(self.validValues))
        else:
            raise ValueError()

class StrListComp(ApComp):
    def __init__(self, name:str, default:list[str], indent:int=0, omitIfEmpty:bool=True):
        # parent
        super().__init__(name, default, indent)
        
        # tweaks
        self.value:list[str] = default
        """The current value of this component."""
        self.omitIfEmpty = omitIfEmpty
        """Whether to skip this field entirely if it's empty"""

    def __repr__(self) -> str:
        ret:str = ""
        prefix:str = ' ' * self.indent
        
        if (len(self.value) == 0):
            if (not self.omitIfEmpty):
                ret = ret + prefix + f"{self.name}: []"
        else:
            ret = ret + prefix + f"{self.name}:"
            for i in self.value:
                ret = ret + "\n" + prefix + f"    - {i}"
        
        return ret

    def set(self, value:list[str]) -> None:
        self.value = value
        
    def get(self) -> list[str]:
        return self.value
    
    def append(self, val:str) -> None:
        """Append val to internal list, unconditionally
        """
        self.value.append(val)
        
    def remove(self, val:str) -> None:
        """Remove first instance of val from internal list. Fails silently if val is not present."""
        try:
            self.value.remove(val)
        except ValueError:
            pass

class PlandoItemComp():
    def __init__(self, items:list[str], locations:list[str], indent:int=0):
       self.indent = indent
       
       self.items = StrListComp("items", items, self.indent + 4)
       self.locations = StrListComp("locations", locations, self.indent + 4)
       
    def __repr__(self) -> str:
        ret:str = ""
        prefix:str = ' ' * self.indent
        
        ret = f"{prefix}-\n"
        ret = ret + f"{self.items}\n"
        ret = ret + f"{self.locations}"
        
        return ret
    
class PlandoItemListComp():
    def __self__(self, indent:int = 0, omitIfEmpty:bool = True):
        self.value:list[PlandoItemComp] = []
        self.omitIfEmpty:bool = omitIfEmpty
        self.indent:int = indent
    
    def __repr__(self) -> str:
        ret:str = ""
        prefix:str = ' ' * self.indent
        
        if (len(self.value) == 0):
            if (not self.omitIfEmpty):
                ret = ret + prefix + f"plando_items: []"
        else:
            ret = ret + prefix + f"plando_items:"
            for i in self.value:
                ret = ret + "\n" + f"{i}"
        return ret
    
    def add(self, items:list[str], locations:list[str]) -> None:
        swp:PlandoItemComp = PlandoItemComp(items, locations, self.indent + 4)
        self.value.append(swp)