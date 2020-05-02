from  RWProcess import *
import os
import pdb

def processFile(baseFile,copyFile):
    data=[]
    #pdb.set_trace()
    procBool,offSet,mdt=readFile(baseFile)
    modTimesinceEpoc = os.path.getmtime(baseFile)
    if float(mdt)<modTimesinceEpoc:

        with open(baseFile,"r") as f1:
            f1.seek(int(offSet))
            data=f1.readlines()
        
        writeFile(baseFile)
 
        with open(copyFile,"a",newline="\n") as f2:
            f2.writelines(data)

processFile("s1.log","dupil.log")

