// -----------------------------------------------------------------------------
// an implementation of some dot notation tooling
//
// greysondn@github
// -----------------------------------------------------------------------------

// guarded imports, because I'll need them
if (not globals.hasIndex("stringUtil")) then
    import "stringUtil"
    globals.stringUtil = stringUtil
end if

// overclever bloody helper object
DotName = {}

DotName.base = ""
DotName.head = []
DotName.tail = ""
DotName.current = 0
DotName.max     = -1

// does this have a next element?
DotName.hasNext = function(self)
    return (self.current <= self.max)
end function

// reset
DotName.reset = function(self)
    self.current = 0
end function

// get next
DotName.getNext = function(self)
    ret = null
    
    if (self.hasNext()) then
        ret = self.head[self.current]
        self.current = self.current + 1
    end if
    
    return ret
end function

// set to string
DotName.set = function(self, dot)
    self.base = dot
    
    self.current = 0
    
    self.head = []
    if (dot.contains(".")) then
        self.head = dot.split(".")
    else
        self.head.push(dot)
    end if
    
    self.tail = self.head.pop()
    
    self.max = self.head.len() - 1
end function

// actual extensions
map.dot_hasIndex = function(self, index)
    ret = false
    
    dot = new DotName
    dot.set(index)
    
    swp = self
    failed = false
    
    while (dot.hasNext() and (not failed))
        nxt = dot.getNext()
        
        if (swp.hasIndex(nxt)) then
            swp = swp[nxt]
        else
            failed = true
        end if
    end while
    
    if (not failed) then
        if (swp.hasIndex(dot.tail)) then
            ret = true
        end if
    end if
    
    return ret
end function

map.dot_get = function(self, index)
    ret = null
    
    dot = new DotName
    dot.set(index)
    
    swp = self
    failed = false
    
    while (dot.hasNext() and (not failed))
        nxt = dot.getNext()
        
        if (swp.hasIndex(nxt)) then
            swp = swp[nxt]
        else
            failed = true
        end if
    end while
    
    if (not failed) then
        if (swp.hasIndex(dot.tail)) then
            ret = swp[dot.tail]
        end if
    end if
    
    return ret
end function

map.dot_set = function(self, index, val)
    dot = new DotName
    dot.set(index)
    
    swp = self
    
    while (dot.hasNext())
        nxt = dot.getNext()
        
        if (not swp.hasIndex(nxt)) then
            swp[nxt] = {}
        end if

        swp = swp[nxt]
    end while
    
    swp[dot.tail] = val
end function

map.dot_createParents = function(self, index)
    dot = new DotName
    dot.set(index)
    
    swp = self
    
    while (dot.hasNext())
        nxt = dot.getNext()
        
        if (not swp.hasIndex(nxt)) then
            swp[nxt] = {}
        end if

        swp = swp[nxt]
    end while
end function

// make it happy we imported this
return {"imported": true}