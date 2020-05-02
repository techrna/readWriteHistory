import os
import csv
import pdb
historyFile="history.csv"




def readFile(fileIn):
    #pdb.set_trace()
    absPath=os.path.abspath(fileIn)
    if os.path.exists(historyFile):
        with  open(historyFile,"r") as file2:
            csvRead=file2.readlines()
            for y in csvRead:
                x= y.split(",")
                print(x)
                if x[0] == absPath:
                    offs=x[2].replace("\n","")
                    return True,offs,x[1]
            return False,0,0
    else :
        return False,0,0

def writeFile(fileIn):
    absPath=os.path.abspath(fileIn)
    modTimesinceEpoc = os.path.getmtime(fileIn)
    file1=open(absPath,"r")
    file1.readlines()
    offset=file1.tell()
    file1.close()
    csvr=[]
    newdata=[]
    rec=[absPath,modTimesinceEpoc,offset]
    if os.path.exists(historyFile):
        with  open(historyFile,"r") as file2:
           csvr=file2.readlines()
           for y in csvr:
               if  y != "\n":
                x=y.split(",")
                print(x)
                if x[0] != absPath :
                   ofs= x[2].replace("\n","")
                   newdata.append([x[0],x[1],ofs])
        newdata.append(rec)

        with  open(historyFile,"w",newline="") as file2:
            csvWrite=csv.writer(file2)
            print(newdata)
            for x in newdata:
                csvWrite.writerow(x)
    else:
        with  open(historyFile,"w+",newline="") as file2:
            csvWrite=csv.writer(file2)
            print(rec)
            csvWrite.writerow(rec)

    

