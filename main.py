from distutils.dir_util import copy_tree
from jsmin import jsmin
from os import listdir, path
from cssmin import cssmin

srcFolder = "src"
distFolder = "dist"

copy_tree(srcFolder, distFolder)

def isChinese(strs):
    if not '\u4e00' <= strs <= '\u9fa5':
        return False
    return True

def checkFile(path:str):
    if path.endswith(".js"):
        with open(path, "r", encoding="UTF8") as f:
            context = f.read()
        with open(path, "w", encoding="UTF8") as f:
            f.write((jsmin(context, quote_chars="'\"`")))
    if path.endswith(".css"):
        with open(path, "r", encoding="UTF8") as f:
            context = f.read()
        with open(path, "w", encoding="UTF8") as f:
            f.write((cssmin(context)))
    if path.endswith(".html"):
        with open(path, "r", encoding="UTF8") as f:
            context = f.read()
        with open(path, "w", encoding="UTF8") as f:
            f.write((context))

def readFolder(folder):
    print(folder)
    for file in listdir(folder):
        filePath = folder+"/"+file
        if path.isdir(filePath):
            readFolder(filePath)
        else:
            checkFile(filePath)

readFolder(distFolder)