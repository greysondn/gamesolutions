// *****************************************************************************
// * wuffma
// * a series of dogmatic "fixes" by a wuff
// *
// * dogma - noun
// * a principle or set of principles laid down by
// * an authority as incontrovertibly true.
// *
// * But I'm not a dog. I'm a wuff.
// *
// * greysondn @ github
// *****************************************************************************

// because this script provides multiple-import guarding, we unfortunately have
// to do the import guards in it via maximum effort.
//
// JoeStrout did provide a way to ensure single imports. See:
// https://miniscript.org/w/index.php?title=Import&oldid=911
//
// I have several complaints about his implementation, even with the same logic.
// So it's used as reference and not outright here.

// ordinary imports, guarded
// -------------------------
if (not globals.hasIndex("listUtil")) then
    globals.listUtil = import "listUtil"
end if

if (not globals.hasIndex("stringUtil")) then
    globals.stringUtil = import "stringUtil"
end if

// and now the actual module, here
// -------------------------------
if (not globals.hasIndex("wuffma")) then
    // we've not imported this module yet
    
    // create originals stash map
    // stash globals in it immediately
    if (not globals.hasIndex("original")) then
        swp = globals.deepCopy()
        globals.original = {}
        globals.original.globals = swp.deepCopy()
    end if
    
    // stashes a copy of an original function in globals.original
    stash = function(mapPath, funcName, func)
        curMap = globals.original
        for i in range(0, mapPath.len - 1)
            if (not curMap.hasIndex(mapPath[i])) then
                curMap[mapPath[i]] = {}
            end if
            
            curMap = curMap[mapPath[i]]
        end for
        
        if (not curMap.hasIndex(funcName))
            // in theory, if it has the index, the most likely explanation is
            // that the stashed version IS the original version
            curMap[funcName] = @func
        endif
    end function
    
    globals.stash = @stash
    
    // import doesn't support subdirectories by default, making it hard to
    // sort code.
    //
    // let's change that in an incomplete, ugly way.
    stash(["builtin"], "import", @import)
    
    import = function(module, force=false)
        // just in case
        ret = false
    
        // back up env vars
        origEnvImportPaths = env.importPaths.deepCopy()
    
        // our real module to import
        realModule = module
    
        // check for dot notation
        if (module.contains(".")) then
            // split the string up
            packs = module.split(".")
            
            // set real module
            realModule = packs[-1]
            
            // slice module off packs
            packs = packs[:-1]
            
            // compose path
            pathTail = ""
            
            for i in range(0, packs.len() - 1)
                pathTail = pathTail + "/" + packs[i]
            end for
            
            // add paths to env.importPaths
            for i in range(0, origEnvImportPaths.len() - 1)
                env.importPaths.push(origEnvImportPaths[i] + pathTail)
            end for
        endif
        
        // check for single import
        if ((force) or (not globals.hasIndex(realModule)) then
            // actually import it
            ret = globals.original.builtin.import realModule
        end if
        
        // and restore the original environment import paths
        env.importPaths= origEnvImportPaths
        
        // and we return
        return ret
    end function
    
    globals.import = @import
    
    // and a partner to make that suck even more
    forceimport = function(module)
        return import(module, true)
    end function
    
    globals.forceimport = @forceimport
    
    // let's change cd, too.
    stash(["builtin"], "cd", @cd)
    
    cd = function(dirPath="")
        globals.original.builtin.cd(dirPath)
        prefix = "com"
    
        if (bot) then
            prefix = "bot"
        end if
    
        endPath = pwd
    
        if (endPath.len > 0) then
            if (endPath[endPath.len - 1] != "/") then
                endPath = endPath + "/"
            end if 
        else
            endPath = endPath + "/"
        end if
    
        globals.env.prompt = prefix + ":" + endPath + "> "
    end function
    
    globals.cd = @cd
    
    // reboot the system, in part by wiping globals and reloading
    globals.reboot = function
        globals = globals.original.globals.deepCopy()
        import "wuffma"
    end function
    
    // and that's it, basically
    import "greysondn.aliases"
    
end if

return {"imported": true}