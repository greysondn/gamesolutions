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

// read user config


if (not globals.hasIndex("wuffma")) then
    // we've not imported this module yet
    
    // create originals stash map
    // stash globals in it immediately
    if (not globals.hasIndex("original")) then
        swp = globals.deepCopy()
        globals.original = {}
        globals.original.globals = swp.deepCopy()
    end if
    
    // read user config into globals
    globals.registry = json.parse(file.open("conf.json").read())

    // support for re-reading registry
    globals.reloadRegistry = function()
        globals.registry = json.parse(file.open("conf.json").read())
    end function
    
    // support for applying registry
    // just the theme right now
    globals.applyRegistry = function()
        text.color = globals.registry.theme.textColor
        text.backColor = globals.registry.theme.backColor
        env.morePrompt = globals.registry.theme.morePrompt
    end function

    // import dot notation helpers
    if (not globals.hasIndex("map_dot")) then
        // doesn't have it yet
        // backup original paths
        origEnvImportPaths = env.importPaths.deepCopy()
        
        // add myself to paths for a moment
        env.importPaths.push("/usr/lib/greysondn/extensions")
        
        // import dot notation
        globals.map_dot = import "map_dot"
        
        // restore original import paths
        env.importPaths = origEnvImportPaths.deepCopy()
    end if



    // stashes a copy of an original function in globals.original
    stash = function(fqn, func)
        if (not globals.original.dot_hasIndex(fqn))
            // in theory, if it has the index, the most likely explanation is
            // that the stashed version IS the original version
            globals.original.dot_set(fqn, @func)
        endif
    end function
    
    globals.stash = @stash
    
    // import doesn't support subdirectories by default, making it hard to
    // sort code.
    //
    // let's change that in an incomplete, ugly way.
    stash(["builtin.import", @import)
    
    import = function(module, force=false, globalize=false)
        // just in case
        ret = false
    
        // back up env vars
        origEnvImportPaths = env.importPaths.deepCopy()
    
        // our real module to import
        tailModule = module
    
        // check for dot notation
        if (module.contains(".")) then
            // split the string up
            packs = module.split(".")
            
            // set real module
            tailModule = packs[-1]
            
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
        if ((force) or (not globals.dot_hasIndex(module)) then
            // actually import it
            ret = globals.original.builtin.import tailModule
            
            if ((not globals.dot_hasIndex(module)) and (globalize)) then
                globals.dot_set(module, ret)
            end if
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
    
    // and a pair of global compliments to that
    globalimport = function(module)
        return globals.import(module, false, true)
    end function
    
    // and again
    globals.globalimport = @globalimport
        return globals.import(module, true, true)
    globalforceimport = function(module)
    
    end function
    
    // let's change cd, too.
    stash("builtin.cd", @cd)
    
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
    
    // fix things according to user conf
    globals.applyRegistry()
    
    // load libs listed to load at boot
    for i in range(0, globals.registry.boot.libs.len() - 1)
        import globals.registry.boot.libs[i]
    end for
end if

return {"imported": true}