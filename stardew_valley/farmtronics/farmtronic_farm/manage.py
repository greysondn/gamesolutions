# python 3.10, meant to run in a pipenv

###
# stupid, bad, dirty management script for my git stuff for farmtronics
#
#
# built against:
# ruamel.yaml
from ruamel.yaml import YAML

import argparse
import os
import shutil
import json

def oneWaySync(sourceHead, destHead, tail):
    '''
    Deletes anything at destination, then copies source to destination.
    Will not make noise on failure, just assumes you know what you're doing.
    Directories have to exist, though. Destructive means you can end up with no
    file at all if source doesn't exist, so... don't use outside some recovery
    mechanism, uh duh.
    '''
    if os.path.exists(destHead + tail):
        os.remove(destHead + tail)
    if os.path.exists(sourceHead + tail):
        shutil.copy2(sourceHead + tail, destHead + tail)
    
def syncFiles(conf, mode):
    gitPth = conf["paths"]["git"]
    svsPth = conf["paths"]["svs"]
    fileList = conf["files"]
    
    # most basic part
    for f in fileList:
        if (mode == "send"):
            oneWaySync(gitPth, svsPth, f)
        elif (mode == "recv"):
            oneWaySync(svsPth, gitPth, f)
        else:
            print("ERR!")
    
    # config requires some special attention
    if (mode == "send"):
        outConf = conf["config"]
        
        confPaths = [svsPth + "conf.json", gitPth + "conf.json"]
        
        for confPath in confPaths:
            if os.path.exists(confPath):
                os.remove(confPath)
            
            with open(confPath, "w", encoding="utf-8") as jf:
                json.dump(
                    outConf,
                    jf,
                    ensure_ascii = False,
                    indent = 4
                )
                
# main function
def main():
    # args
    parser = argparse.ArgumentParser(
        description = "Helper to manage code and repo for farmtronics. " +
                      "Configure via conf.yaml."
    )

    subparsers = parser.add_subparsers(
        help="Command to run",
        dest="action"
    )
    
    parser.recv = subparsers.add_parser(
        "recv",
        help="Move files from Stardew Valley save directory into git repo."
    )
    
    parser_send = subparsers.add_parser(
        "send",
        help = "Convert and move files into Stardew Valley save directory."
    )

    args = parser.parse_args()

    # config
    yaml=YAML(typ='safe')
    conf = None
    with open("conf.yaml") as f:
         conf = yaml.load(f)
    
    # and then we do the things here.
    #
    # args is the parser args.
    # conf is config
    if (args.action == "send"):
        syncFiles(conf, "send")
    elif (args.action == "recv"):
        syncFiles(conf, "recv")
    else:
        print(f"ARGS ERR! {args}")

# main guard
if (__name__ == "__main__"):
    main()