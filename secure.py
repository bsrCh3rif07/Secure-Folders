import base64
import os
import time
import sys
import subprocess
def RunF(s):
    subprocess.Popen("batch.bat", cwd=s)
    print("Done !")

def SetPasswordInTheFolder(f):
    s = str(f) + '\\' + 'f.bat'
    pw = input("Enter your password for Lock your folder: ").encode('ascii')
    encode = base64.b64encode(pw).decode('ascii')
    os.chdir(f)
    f = open("f.bat","w")
    #use = open('UsefullDoc.txt','r').readlines()
    a = "cls \n @ECHO OFF \n title Folder Locker \n if EXIST \"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}\" goto UNLOCK \n if NOT EXIST Locker goto MDLOCKER \n :CONFIRM  \n echo Are you sure u want to Lock the folder(Y/N) \n set/p \"cho=>\" \n if %cho%==Y goto LOCK \n if %cho%==y goto LOCK \n if %cho%==n goto END \n if %cho%==N goto END \n echo Invalid choice. \n goto CONFIRM \n :LOCK \n ren Locker \"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}\" \n attrib +h +s \"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}\" \n echo Folder locked \n goto End \n :UNLOCK \n echo Enter password to Unlock folder \n set/p \"pass=>\" \n if NOT %pass%=="+str(encode)+" goto FAIL \n attrib -h -s \"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}\" \n ren \"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}\" Locker \n echo Folder Unlocked successfully \n goto End \n :FAIL \n echo Invalid password \n goto end \n :MDLOCKER \n md Locker \n echo Locker created successfully \n goto End \n :End"
    f.write(a)
    #RunF(s)

folder = str(input("Enter your path folder name: "))
if not os.path.exists(folder):
    print("Error your folder does not existe")
    while 1:
        path = str(input("Enter the path to place your new folder"))
        if os.path.exists(path):
            folderN = str(input("Enter your folder name: "))
            folder = path + '\\' + folderN
            os.mkdir(folder)
            SetPasswordInTheFolder(folder)
            sys.exit(1)
        print("Error your path does not existe")
else:
    SetPasswordInTheFolder(folder)